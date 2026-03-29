#!/usr/bin/env python3
"""
DFIR Watchtower — Automated threat intel & forensics content aggregator
Author: Bryan Ambrose (D.Sc., GCFA, GCFR, OSCP)
Purpose: Monitor DFIR blogs, threat intel feeds, and forensic tool updates.
         Identify new content within a configurable lookback window and
         generate a formatted HTML digest report.

Usage:
    python3 watchtower.py                  # default: last 7 days, HTML output
    python3 watchtower.py --days 3         # last 3 days
    python3 watchtower.py --days 1         # last 24 hours
    python3 watchtower.py --output report.html
    python3 watchtower.py --markdown       # also emit a .md digest
"""

import argparse
import html
import logging
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Optional
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("watchtower")

# ---------------------------------------------------------------------------
# Source registry
# Each entry: (label, url, fetch_strategy)
#   fetch_strategy: "rss" | "atom" | "html_blog" | "brutalist" | "startme"
# ---------------------------------------------------------------------------
SOURCES = [
    # ── RSS / Atom feeds ────────────────────────────────────────────────────
    {
        "label": "MyDFIR",
        "url": "https://mydfir.com/feed/",
        "strategy": "rss",
        "category": "Blog",
    },
    {
        "label": "InfoSec Write-ups (Medium)",
        "url": "https://medium.com/feed/infosec-writeups",
        "strategy": "rss",
        "category": "Blog",
    },
    {
        "label": "r/computerforensics",
        "url": "https://www.reddit.com/r/computerforensics/.rss",
        "strategy": "rss",
        "category": "Community",
    },
    {
        "label": "r/netsec",
        "url": "https://www.reddit.com/r/netsec/.rss",
        "strategy": "rss",
        "category": "Community",
    },
    {
        "label": "r/blueteamsec",
        "url": "https://www.reddit.com/r/blueteamsec/.rss",
        "strategy": "rss",
        "category": "Community",
    },
    {
        "label": "r/Malware",
        "url": "https://www.reddit.com/r/Malware/.rss",
        "strategy": "rss",
        "category": "Community",
    },
    {
        "label": "CISA Cybersecurity Advisories",
        "url": "https://www.cisa.gov/cybersecurity-advisories/advisories.xml",
        "strategy": "rss",
        "category": "Threat Intel",
    },
    # ── HTML-scraped blogs ───────────────────────────────────────────────────
    {
        "label": "This Week in 4n6",
        "url": "https://thisweekin4n6.com/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://thisweekin4n6.com/feed/",
    },
    {
        "label": "AboutDFIR",
        "url": "https://aboutdfir.com/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://aboutdfir.com/feed/",
    },
    {
        "label": "Forensic Focus",
        "url": "https://forensicfocus.com/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://www.forensicfocus.com/feed/",
    },
    {
        "label": "Baker Street Forensics",
        "url": "https://bakerstreetforensics.com/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://bakerstreetforensics.com/feed/",
    },
    {
        "label": "Stark 4N6 (Kevin Pagano)",
        "url": "https://stark4n6.com/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://stark4n6.com/feed/",
    },
    {
        "label": "DFIR Dominican (Fabian Mendoza)",
        "url": "https://dfirminican.com/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://dfirminican.com/feed/",
    },
    {
        "label": "Cyber Triage Blog",
        "url": "https://www.cybertriage.com/blog/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://www.cybertriage.com/feed/",
    },
    {
        "label": "The Eclectic Light Company (macOS)",
        "url": "https://eclecticlight.co/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://eclecticlight.co/feed/",
    },
    {
        "label": "Forensafe",
        "url": "https://forensafe.com/",
        "strategy": "html_blog",
        "category": "Blog",
        "rss_fallback": "https://forensafe.com/feed/",
    },
    # ── Special scrapers ─────────────────────────────────────────────────────
    {
        "label": "Brutalist Report — Tech",
        "url": "https://brutalist.report/topic/tech",
        "strategy": "brutalist",
        "category": "Aggregator",
    },
    {
        "label": "Start.me DFIR Forensics Feed",
        "url": "https://start.me/p/q6mw4Q/forensics",
        "strategy": "startme",
        "category": "Aggregator",
    },
]

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; DFIRWatchtower/1.0; "
        "+https://github.com/bryan-ambrose/DFIR_Tools)"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

REDDIT_HEADERS = {
    "User-Agent": "DFIRWatchtower/1.0 (by /u/dfir_watchtower)",
}

TIMEOUT = 20  # seconds


def fetch_url(url: str, extra_headers: dict = None) -> Optional[str]:
    """Fetch a URL and return the raw text content, or None on failure."""
    headers = {**HEADERS, **(extra_headers or {})}
    try:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.HTTPError as e:
        log.warning(f"HTTP {e.response.status_code} for {url}")
    except requests.exceptions.ConnectionError:
        log.warning(f"Connection error for {url}")
    except requests.exceptions.Timeout:
        log.warning(f"Timeout for {url}")
    except Exception as e:
        log.warning(f"Error fetching {url}: {e}")
    return None


# ---------------------------------------------------------------------------
# Date parsing utilities
# ---------------------------------------------------------------------------
def parse_date(date_str: str) -> Optional[datetime]:
    """Try multiple date formats and return UTC-aware datetime or None."""
    if not date_str:
        return None
    date_str = date_str.strip()

    # RFC 2822 (RSS pubDate)
    try:
        dt = parsedate_to_datetime(date_str)
        return dt.astimezone(timezone.utc)
    except Exception:
        pass

    # ISO 8601 variants
    iso_formats = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ]
    for fmt in iso_formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            pass

    return None


def within_window(dt: Optional[datetime], cutoff: datetime) -> bool:
    """Return True if dt is after the cutoff (i.e., within the lookback window)."""
    if dt is None:
        return True  # include undated items rather than silently drop them
    return dt >= cutoff


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
class FeedItem:
    __slots__ = ("title", "url", "published", "summary", "source", "category")

    def __init__(self, title, url, published, summary, source, category):
        self.title = title or "(no title)"
        self.url = url or ""
        self.published = published
        self.summary = summary or ""
        self.source = source
        self.category = category

    def pub_str(self) -> str:
        if self.published:
            return self.published.strftime("%Y-%m-%d %H:%M UTC")
        return "Unknown date"


# ---------------------------------------------------------------------------
# RSS / Atom parser (no feedparser dependency)
# ---------------------------------------------------------------------------
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "media": "http://search.yahoo.com/mrss/",
}


def _text(el, *tags) -> str:
    """Try a list of tag names and return the first non-empty text."""
    if el is None:
        return ""
    for tag in tags:
        child = el.find(tag)
        if child is not None and child.text:
            return child.text.strip()
    return ""


def _attr(el, tag, attr) -> str:
    if el is None:
        return ""
    child = el.find(tag)
    if child is not None:
        return child.get(attr, "")
    return ""


def parse_rss_atom(xml_text: str, source_label: str, category: str,
                   cutoff: datetime) -> list[FeedItem]:
    """Parse RSS 2.0 or Atom 1.0 XML and return FeedItems within the window."""
    items = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        log.warning(f"XML parse error for {source_label}: {e}")
        return items

    tag = root.tag.lower()

    # ── Atom ────────────────────────────────────────────────────────────────
    if "atom" in tag or root.tag == "{http://www.w3.org/2005/Atom}feed":
        atom_ns = "http://www.w3.org/2005/Atom"
        for entry in root.findall(f"{{{atom_ns}}}entry"):
            title_el = entry.find(f"{{{atom_ns}}}title")
            title = title_el.text.strip() if title_el is not None and title_el.text else ""

            # link: prefer rel=alternate or first href
            link = ""
            for link_el in entry.findall(f"{{{atom_ns}}}link"):
                rel = link_el.get("rel", "alternate")
                if rel in ("alternate", ""):
                    link = link_el.get("href", "")
                    break
            if not link:
                link_el = entry.find(f"{{{atom_ns}}}link")
                if link_el is not None:
                    link = link_el.get("href", "")

            updated_el = entry.find(f"{{{atom_ns}}}updated") or entry.find(f"{{{atom_ns}}}published")
            pub = parse_date(updated_el.text if updated_el is not None else "")

            summary_el = (entry.find(f"{{{atom_ns}}}summary") or
                          entry.find(f"{{{atom_ns}}}content"))
            raw_summary = summary_el.text if summary_el is not None else ""
            summary = _strip_html(raw_summary)[:300]

            if within_window(pub, cutoff):
                items.append(FeedItem(title, link, pub, summary, source_label, category))
        return items

    # ── RSS 2.0 ─────────────────────────────────────────────────────────────
    channel = root.find("channel")
    if channel is None:
        channel = root  # some feeds omit <channel>

    for item in channel.findall("item"):
        title = _text(item, "title")
        link = _text(item, "link")
        if not link:
            # guid sometimes holds the URL
            guid_el = item.find("guid")
            if guid_el is not None and guid_el.get("isPermaLink", "true") == "true":
                link = guid_el.text or ""

        pub_str = _text(item, "pubDate", "dc:date",
                        "{http://purl.org/dc/elements/1.1/}date")
        pub = parse_date(pub_str)

        # summary: description → content:encoded → dc:description
        desc_el = (item.find("description") or
                   item.find("{http://purl.org/rss/1.0/modules/content/}encoded") or
                   item.find("{http://purl.org/dc/elements/1.1/}description"))
        raw_desc = desc_el.text if desc_el is not None else ""
        summary = _strip_html(raw_desc)[:300]

        if within_window(pub, cutoff):
            items.append(FeedItem(title, link, pub, summary, source_label, category))

    return items


def _strip_html(raw: str) -> str:
    """Strip HTML tags and decode entities from a string."""
    if not raw:
        return ""
    try:
        soup = BeautifulSoup(raw, "lxml")
        return soup.get_text(separator=" ").strip()
    except Exception:
        return html.unescape(raw)


# ---------------------------------------------------------------------------
# HTML blog scraper (tries RSS fallback first, then DOM heuristic)
# ---------------------------------------------------------------------------
def scrape_html_blog(source: dict, cutoff: datetime) -> list[FeedItem]:
    label = source["label"]
    category = source["category"]

    # 1) Try RSS/Atom fallback URL first (most WordPress blogs expose /feed/)
    rss_url = source.get("rss_fallback")
    if rss_url:
        log.info(f"  → Trying RSS fallback: {rss_url}")
        raw = fetch_url(rss_url)
        if raw:
            items = parse_rss_atom(raw, label, category, cutoff)
            if items:
                log.info(f"  ✓ {len(items)} items via RSS for {label}")
                return items

    # 2) Fallback: scrape the main HTML page for article links + dates
    log.info(f"  → HTML scraping: {source['url']}")
    raw = fetch_url(source["url"])
    if not raw:
        return []

    soup = BeautifulSoup(raw, "lxml")
    items = []

    # Heuristic: find <article> tags or <h2>/<h3> containing <a> links
    articles = soup.find_all("article") or soup.find_all(class_=lambda c: c and "post" in c.lower())

    if articles:
        for art in articles[:20]:
            # title + link
            heading = art.find(["h1", "h2", "h3"])
            a_tag = heading.find("a") if heading else art.find("a")
            title = a_tag.get_text(strip=True) if a_tag else ""
            link = a_tag.get("href", "") if a_tag else ""
            if link and not link.startswith("http"):
                from urllib.parse import urljoin
                link = urljoin(source["url"], link)

            # date
            time_el = art.find("time")
            pub_str = ""
            if time_el:
                pub_str = time_el.get("datetime", time_el.get_text(strip=True))
            pub = parse_date(pub_str)

            # snippet
            p_tag = art.find("p")
            summary = p_tag.get_text(strip=True)[:300] if p_tag else ""

            if title and link and within_window(pub, cutoff):
                items.append(FeedItem(title, link, pub, summary, label, category))
    else:
        # Ultra-fallback: grab all anchor links with recognizable blog path patterns
        for a in soup.find_all("a", href=True)[:50]:
            href = a["href"]
            text = a.get_text(strip=True)
            if (len(text) > 20 and
                    ("/" in href) and
                    not href.startswith("#") and
                    not href.startswith("mailto")):
                if not href.startswith("http"):
                    from urllib.parse import urljoin
                    href = urljoin(source["url"], href)
                items.append(FeedItem(text, href, None, "", label, category))

    log.info(f"  ✓ {len(items)} items via HTML scrape for {label}")
    return items[:15]  # cap to avoid noise


# ---------------------------------------------------------------------------
# Brutalist Report scraper
# ---------------------------------------------------------------------------
def scrape_brutalist(source: dict, cutoff: datetime) -> list[FeedItem]:
    label = source["label"]
    category = source["category"]
    log.info(f"  → Brutalist Report scrape: {source['url']}")
    raw = fetch_url(source["url"])
    if not raw:
        return []

    soup = BeautifulSoup(raw, "lxml")
    items = []

    # Brutalist Report uses simple <a> links inside a <main>/<div class="brutalist-...">
    main = soup.find("main") or soup.find("div", class_=lambda c: c and "content" in (c or "").lower()) or soup
    for a in main.find_all("a", href=True)[:60]:
        href = a["href"]
        text = a.get_text(strip=True)
        if (len(text) > 10 and
                href.startswith("http") and
                "brutalist.report" not in href):
            items.append(FeedItem(text, href, None, "", label, category))

    log.info(f"  ✓ {len(items)} items from Brutalist Report")
    return items[:20]


# ---------------------------------------------------------------------------
# Start.me scraper (public page — extracts visible links)
# ---------------------------------------------------------------------------
def scrape_startme(source: dict, cutoff: datetime) -> list[FeedItem]:
    label = source["label"]
    category = source["category"]
    log.info(f"  → start.me scrape: {source['url']}")
    raw = fetch_url(source["url"])
    if not raw:
        return []

    soup = BeautifulSoup(raw, "lxml")
    items = []

    # start.me renders content via JS — look for any <a> links in the payload
    # that reference external forensics resources
    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = a.get_text(strip=True)
        if (len(text) > 10 and
                href.startswith("http") and
                "start.me" not in href):
            items.append(FeedItem(text, href, None, "", label, category))

    if not items:
        log.warning(f"  start.me returned no links (likely JS-rendered); "
                    f"consider using a headless browser for this source.")

    log.info(f"  ✓ {len(items)} items from start.me")
    return items[:30]


# ---------------------------------------------------------------------------
# Main fetcher dispatcher
# ---------------------------------------------------------------------------
def fetch_source(source: dict, cutoff: datetime) -> list[FeedItem]:
    log.info(f"Fetching: {source['label']} ({source['strategy']})")
    strategy = source["strategy"]

    if strategy in ("rss", "atom"):
        headers = REDDIT_HEADERS if "reddit.com" in source["url"] else None
        raw = fetch_url(source["url"], extra_headers=headers)
        if not raw:
            return []
        items = parse_rss_atom(raw, source["label"], source["category"], cutoff)
        log.info(f"  ✓ {len(items)} items from {source['label']}")
        return items

    elif strategy == "html_blog":
        return scrape_html_blog(source, cutoff)

    elif strategy == "brutalist":
        return scrape_brutalist(source, cutoff)

    elif strategy == "startme":
        return scrape_startme(source, cutoff)

    else:
        log.warning(f"Unknown strategy '{strategy}' for {source['label']}")
        return []


# ---------------------------------------------------------------------------
# HTML Report Generator
# ---------------------------------------------------------------------------
CATEGORY_COLORS = {
    "Blog": "#2563eb",
    "Community": "#7c3aed",
    "Threat Intel": "#dc2626",
    "Aggregator": "#0891b2",
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DFIR Watchtower Digest — {date_str}</title>
<style>
  :root {{
    --bg: #0f172a;
    --surface: #1e293b;
    --surface2: #334155;
    --accent: #38bdf8;
    --text: #e2e8f0;
    --muted: #94a3b8;
    --border: #334155;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
  }}
  header {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-bottom: 2px solid var(--accent);
    padding: 2rem;
    text-align: center;
  }}
  header h1 {{
    font-size: 2rem;
    color: var(--accent);
    letter-spacing: 0.05em;
  }}
  header p {{ color: var(--muted); margin-top: 0.5rem; }}
  .stats {{
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1rem;
    flex-wrap: wrap;
  }}
  .stat {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.75rem 1.5rem;
    text-align: center;
  }}
  .stat .val {{ font-size: 1.5rem; font-weight: 700; color: var(--accent); }}
  .stat .lbl {{ font-size: 0.75rem; color: var(--muted); text-transform: uppercase; }}
  main {{ max-width: 1100px; margin: 2rem auto; padding: 0 1rem; }}
  .section-header {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 2rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
  }}
  .section-header h2 {{ font-size: 1.25rem; }}
  .badge {{
    font-size: 0.7rem;
    padding: 0.2rem 0.6rem;
    border-radius: 999px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #fff;
  }}
  .source-group {{ margin-bottom: 2rem; }}
  .source-name {{
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.5rem;
  }}
  .item {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.875rem 1rem;
    margin-bottom: 0.5rem;
    transition: border-color 0.15s;
  }}
  .item:hover {{ border-color: var(--accent); }}
  .item a {{
    color: var(--text);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.95rem;
  }}
  .item a:hover {{ color: var(--accent); }}
  .item-meta {{
    display: flex;
    gap: 1rem;
    margin-top: 0.35rem;
    font-size: 0.78rem;
    color: var(--muted);
    flex-wrap: wrap;
  }}
  .item-summary {{
    font-size: 0.83rem;
    color: var(--muted);
    margin-top: 0.4rem;
    line-height: 1.5;
  }}
  .no-items {{
    color: var(--muted);
    font-style: italic;
    font-size: 0.9rem;
    padding: 0.5rem 0;
  }}
  footer {{
    text-align: center;
    padding: 2rem;
    color: var(--muted);
    font-size: 0.8rem;
    border-top: 1px solid var(--border);
    margin-top: 3rem;
  }}
  footer a {{ color: var(--accent); text-decoration: none; }}
  .toc {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem 1.5rem;
    margin-bottom: 2rem;
  }}
  .toc h3 {{ font-size: 0.9rem; color: var(--muted); margin-bottom: 0.5rem; text-transform: uppercase; }}
  .toc ul {{ list-style: none; display: flex; flex-wrap: wrap; gap: 0.5rem 1.5rem; }}
  .toc a {{ color: var(--accent); text-decoration: none; font-size: 0.85rem; }}
  .toc a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<header>
  <h1>🔭 DFIR Watchtower</h1>
  <p>Digest for <strong>{date_str}</strong> &mdash; lookback window: <strong>{days} day(s)</strong></p>
  <div class="stats">
    <div class="stat"><div class="val">{total_items}</div><div class="lbl">Total Items</div></div>
    <div class="stat"><div class="val">{total_sources}</div><div class="lbl">Sources Scanned</div></div>
    <div class="stat"><div class="val">{sources_with_items}</div><div class="lbl">Sources w/ New Content</div></div>
    <div class="stat"><div class="val">{run_time}s</div><div class="lbl">Scan Time</div></div>
  </div>
</header>
<main>
  {toc_html}
  {body_html}
</main>
<footer>
  Generated by <strong>DFIR Watchtower</strong> &mdash;
  <a href="https://github.com/bryan-ambrose/DFIR_Tools">github.com/bryan-ambrose/DFIR_Tools</a>
  &mdash; {timestamp}
</footer>
</body>
</html>"""


def render_html(
    results: dict[str, list[FeedItem]],
    days: int,
    run_time: float,
) -> str:
    """Render a full HTML digest from results dict keyed by source label."""
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%Y-%m-%d %H:%M UTC")

    total_items = sum(len(v) for v in results.values())
    total_sources = len(results)
    sources_with_items = sum(1 for v in results.values() if v)

    # Group by category
    categories: dict[str, dict[str, list[FeedItem]]] = {}
    for source in SOURCES:
        label = source["label"]
        cat = source["category"]
        if cat not in categories:
            categories[cat] = {}
        if label in results:
            categories[cat][label] = results[label]

    # TOC
    toc_links = []
    for cat in categories:
        anchor = cat.lower().replace(" ", "-")
        toc_links.append(f'<li><a href="#{anchor}">{cat}</a></li>')
    toc_html = (
        '<div class="toc"><h3>Categories</h3>'
        f'<ul>{"".join(toc_links)}</ul></div>'
    )

    # Body
    body_parts = []
    for cat, sources in categories.items():
        anchor = cat.lower().replace(" ", "-")
        color = CATEGORY_COLORS.get(cat, "#64748b")
        count = sum(len(v) for v in sources.values())
        badge_html = (
            f'<span class="badge" style="background:{color}">{cat}</span>'
        )
        body_parts.append(
            f'<div class="section-header" id="{anchor}">'
            f'<h2>{badge_html} {html.escape(cat)}</h2>'
            f'<span style="color:var(--muted);font-size:0.85rem">{count} item(s)</span>'
            f'</div>'
        )

        for label, items in sources.items():
            body_parts.append('<div class="source-group">')
            body_parts.append(f'<div class="source-name">{html.escape(label)}</div>')
            if not items:
                body_parts.append('<div class="no-items">No new items in this window.</div>')
            else:
                for item in items:
                    summary_html = ""
                    if item.summary:
                        escaped = html.escape(item.summary[:280])
                        summary_html = f'<div class="item-summary">{escaped}…</div>'
                    body_parts.append(
                        f'<div class="item">'
                        f'<a href="{html.escape(item.url)}" target="_blank" rel="noopener">'
                        f'{html.escape(item.title)}</a>'
                        f'<div class="item-meta">'
                        f'<span>🕐 {html.escape(item.pub_str())}</span>'
                        f'<span>🔗 <a href="{html.escape(item.url)}" target="_blank" '
                        f'rel="noopener" style="color:var(--muted)">{html.escape(item.url[:70])}</a></span>'
                        f'</div>'
                        f'{summary_html}'
                        f'</div>'
                    )
            body_parts.append("</div>")

    body_html = "\n".join(body_parts)

    return HTML_TEMPLATE.format(
        date_str=date_str,
        days=days,
        total_items=total_items,
        total_sources=total_sources,
        sources_with_items=sources_with_items,
        run_time=f"{run_time:.1f}",
        toc_html=toc_html,
        body_html=body_html,
        timestamp=timestamp,
    )


# ---------------------------------------------------------------------------
# Markdown digest generator
# ---------------------------------------------------------------------------
def render_markdown(results: dict[str, list[FeedItem]], days: int) -> str:
    now = datetime.now(timezone.utc)
    lines = [
        f"# 🔭 DFIR Watchtower Digest — {now.strftime('%Y-%m-%d')}",
        f"\n> Lookback: **{days} day(s)** | Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
    ]

    categories: dict[str, dict[str, list[FeedItem]]] = {}
    for source in SOURCES:
        label = source["label"]
        cat = source["category"]
        if cat not in categories:
            categories[cat] = {}
        if label in results:
            categories[cat][label] = results[label]

    for cat, sources in categories.items():
        lines.append(f"\n## {cat}\n")
        for label, items in sources.items():
            lines.append(f"### {label}\n")
            if not items:
                lines.append("_No new items in this window._\n")
            else:
                for item in items:
                    pub = item.pub_str()
                    lines.append(f"- **[{item.title}]({item.url})**  ")
                    lines.append(f"  _{pub}_")
                    if item.summary:
                        lines.append(f"  {item.summary[:200]}…")
                    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="DFIR Watchtower — automated DFIR content aggregator"
    )
    parser.add_argument(
        "--days", type=int, default=7,
        help="Lookback window in days (default: 7)"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Output HTML file path (default: auto-named in CWD)"
    )
    parser.add_argument(
        "--markdown", action="store_true",
        help="Also emit a Markdown (.md) digest alongside the HTML"
    )
    parser.add_argument(
        "--sources", nargs="+",
        help="Only scrape specific source labels (partial match, case-insensitive)"
    )
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    log.info(f"DFIR Watchtower starting — lookback: {args.days} day(s), cutoff: {cutoff.strftime('%Y-%m-%d %H:%M UTC')}")

    # Filter sources if requested
    active_sources = SOURCES
    if args.sources:
        filters = [f.lower() for f in args.sources]
        active_sources = [
            s for s in SOURCES
            if any(f in s["label"].lower() for f in filters)
        ]
        log.info(f"Filtered to {len(active_sources)} source(s)")

    # Fetch all sources
    t0 = time.time()
    results: dict[str, list[FeedItem]] = {}
    for source in active_sources:
        items = fetch_source(source, cutoff)
        results[source["label"]] = items
        # Small polite delay between requests
        time.sleep(0.5)

    run_time = time.time() - t0
    total = sum(len(v) for v in results.values())
    log.info(f"Done. {total} items collected in {run_time:.1f}s")

    # Determine output paths
    date_slug = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if args.output:
        html_path = Path(args.output)
    else:
        html_path = Path(f"watchtower_digest_{date_slug}.html")

    md_path = html_path.with_suffix(".md")

    # Render and write HTML
    html_content = render_html(results, args.days, run_time)
    html_path.write_text(html_content, encoding="utf-8")
    log.info(f"HTML digest written → {html_path}")

    # Optionally render Markdown
    if args.markdown:
        md_content = render_markdown(results, args.days)
        md_path.write_text(md_content, encoding="utf-8")
        log.info(f"Markdown digest written → {md_path}")

    print(f"\n✅  DFIR Watchtower complete.")
    print(f"    Items collected : {total}")
    print(f"    HTML report     : {html_path.resolve()}")
    if args.markdown:
        print(f"    Markdown report : {md_path.resolve()}")


if __name__ == "__main__":
    main()
