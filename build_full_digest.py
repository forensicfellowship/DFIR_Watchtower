#!/usr/bin/env python3
"""DFIR Watchtower – weekly digest builder (2026-03-29)"""
import html
import re
from pathlib import Path
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc)
DATE_STR = NOW.strftime("%Y-%m-%d")
PULLED = NOW.strftime("%Y-%m-%d %H:%M UTC")

# ─── SECTION COLORS ──────────────────────────────────────────────────────────
SECTION_COLORS = {
    "FORENSIC ANALYSIS": "#0e7490",
    "THREAT INTELLIGENCE / HUNTING": "#dc2626",
    "UPCOMING EVENTS": "#7c3aed",
    "PRESENTATIONS / PODCASTS": "#2563eb",
    "MALWARE": "#b45309",
    "MISCELLANEOUS": "#047857",
    "SOFTWARE UPDATES": "#1d4ed8",
}

# ─── COMMUNITY CHANNELS ──────────────────────────────────────────────────────
COMMUNITY_CHANNELS = [
    {"name": "r/computerforensics", "url": "https://www.reddit.com/r/computerforensics/", "members": "60k+", "description": "Case discussions, tool Q&A, and career advice for digital forensics practitioners.", "color": "#0e7490"},
    {"name": "r/blueteamsec", "url": "https://www.reddit.com/r/blueteamsec/", "members": "45k+", "description": "High-signal defensive security: threat intel, detection engineering, and incident response links.", "color": "#2563eb"},
    {"name": "r/netsec", "url": "https://www.reddit.com/r/netsec/", "members": "500k+", "description": "Technical information security content — research papers, exploits, tooling, and write-ups.", "color": "#dc2626"},
    {"name": "r/Malware", "url": "https://www.reddit.com/r/Malware/", "members": "85k+", "description": "Malware analysis, reverse engineering samples, and threat actor discussions.", "color": "#b45309"},
    {"name": "r/cybersecurity", "url": "https://www.reddit.com/r/cybersecurity/", "members": "1M+", "description": "Broad security community: news, certifications, career paths, and industry happenings.", "color": "#047857"},
    {"name": "r/ReverseEngineering", "url": "https://www.reddit.com/r/ReverseEngineering/", "members": "200k+", "description": "Reversing tools, CTF write-ups, binary analysis, and low-level debugging techniques.", "color": "#7c3aed"},
]

# ─── WEEK 13 DATA (2026-03-29) ────────────────────────────────────────────────
W_LATEST = {
    "name": "29 March 2026",
    "date": "This Week in 4n6",
    "url": "https://thisweekin4n6.com/2026/03/29/week-13-2026/",
    "sections": [
        {
            "heading": "FORENSIC ANALYSIS",
            "items": [
                ["Shall I describe it to you …? ALEAPP Live Data Parsing", "https://cp-df.com/en/blog/dumpsys.html"],
                ["Android Any.do", "https://forensafe.com/blogs/android-anydo.html"],
                ["Exploring Apple Intelligence Artifacts in iOS", "https://dig-fo4-6.blogspot.com/2026/03/exploring-apple-intelligence-artifacts.html"],
                ["Linux Forensic Scenario", "https://righteousit.com/2026/03/27/linux-forensic-scenario/"],
                ["[13 Cubed] Trouble at ACME Challenge — Investigating Windows Endpoint", "https://infosecwriteups.com/13-cubed-trouble-at-acme-challenge-investigating-windows-endpoint-9cada1bcd47b"],
                ["FAT CAT (Forensics)— KJSSE CTF 3.0", "https://infosecwriteups.com/fat-cat-forensics-kjsse-ctf-3-0-389909256dc5"],
                ["Old Dog, New Tricks – Lost Apples 2.0", "https://thebinaryhick.blog/2026/03/22/old-dog-new-tricks-lost-apples-2-0/"],
                ["MSAB Mobile Forensics Summit CTF 2026 Android CTF Writeup", "https://matthewplascencia.substack.com/p/msab-mobile-forensics-summit-ctf"],
                ["Bloomin' Biomes – Meet Sedgwick", "https://northloopconsulting.com/blog/f/bloomin-biomes---meet-sedgwick"],
                ["ShellBags and User Navigation: What Windows Remembers About Exploration", "https://sethenoka.com/shellbags-and-user-navigation-what-windows-remembers-about-exploration/"],
                ["Kubernetes forensics 1/3 : what the container ?", "https://www.synacktiv.com/publications/kubernetes-forensics-13-what-the-container.html"],
            ]
        },
        {
            "heading": "THREAT INTELLIGENCE / HUNTING",
            "items": [
                ["ESC8s and Where to Find Them", "http://abdulmhsblog.com/posts/esc8andfindingwebenrollmentendpoints/"],
                ["CanisterWorm Gets Teeth: TeamPCP's Kubernetes Wiper Targets Iran", "https://www.aikido.dev/blog/teampcp-stage-payload-canisterworm-iran"],
                ["Popular telnyx package compromised on PyPI by TeamPCP", "https://www.aikido.dev/blog/telnyx-pypi-compromised-teampcp-canisterworm"],
                ["The AI Malware Surge: Behavior, Attribution, and Defensive Readiness", "https://arcticwolf.com/resources/blog/the-ai-malware-surge-behavior-attribution-and-defensive-readiness/"],
                ["What Does MITRE ATT&CK Coverage Really Mean?", "https://www.attackiq.com/2026/03/10/what-does-mitre-attack-coverage-really-mean/"],
                ["Ransomware Attacks Against the US: 2026 Insights", "https://www.bitdefender.com/en-us/blog/businessinsights/ransomware-attacks-targeting-us-organizations-2026"],
                ["'CanisterWorm' Springs Wiper Attack Targeting Iran", "https://krebsonsecurity.com/2026/03/canisterworm-springs-wiper-attack-targeting-iran/"],
                ["Under CTRL: Dissecting a Previously Undocumented Russian .Net Access Framework", "https://censys.com/blog/under-ctrl-dissecting-a-previously-undocumented-russian-net-access-framework/"],
                ["Кібератака UAC-0255 під виглядом сповіщення від CERT-UA", "https://cert.gov.ua/article/6288047"],
                ["23rd March – Threat Intelligence Report", "https://research.checkpoint.com/2026/23rd-march-threat-intelligence-report/"],
                ["North America's Cyber Security Threat Reality in 2026", "https://blog.checkpoint.com/research/north-americas-cyber-security-threat-reality-in-2026/"],
                ["Credential Phishing", "https://ogmini.github.io/2026/03/26/Credential-Phishing.html"],
                ["2025 Talos Year in Review: Speed, scale, and staying power", "https://blog.talosintelligence.com/2025-talos-year-in-review-speed-scale-and-staying-power/"],
                ["p6.arpa Wildcard Abuse: Hunting Phishing Infrastructure Across IPv6 Prefixes", "https://www.cloudsek.com/blog/p6-arpa-wildcard-abuse-hunting-phishing-infrastructure-across-ipv6-prefixes"],
                ["Honey for Hackers: A Study of Attacks Targeting CVE-2026-21962", "https://www.cloudsek.com/blog/honey-for-hackers-cve-2026-21962-weblogic"],
                ["The Unintentional Enabler: How Cloudflare Services are Abused for Credential Theft", "https://cofense.com/blog/the-unintentional-enabler-cloudflare-phishing/"],
                ["Common Entra ID Security Assessment Findings – Part 1", "https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1/"],
                ["Tracking Software Weaponized by Criminals", "https://www.confiant.com/news/tracking-software-weaponized-by-criminals"],
                ["Understanding and detecting process injection with Sysmon", "https://www.cyberbit.com/security-operations/process-injection-with-sysmon/"],
                ["TeamPCP Injects Credential Stealer Into Trivy Releases and Spreads to npm", "https://cybersecsentinel.com/teampcp-injects-credential-stealer-into-trivy-releases-and-spreads-to-npm-via-canisterworm/"],
                ["The Energy Sector's Ransomware Nightmare", "https://cyble.com/blog/energy-sector-ransomware-attack-report/"],
                ["China's APT41 and the Expanding Enterprise Attack Surface", "https://cyble.com/blog/apt41-enterprise-attack-surface-cyber-risk/"],
                ["BreachForums Data Leaks: Technical Analysis and Timeline Attribution (2022–2026)", "https://www.d3lab.net/breachforums-data-leaks-technical-analysis-and-timeline-attribution-2022-2026/"],
                ["Tracking & Detecting GhostSocks Malware", "https://www.darktrace.com/blog/phantom-footprints-tracking-ghostsocks-malware"],
                ["LiteLLM compromised on PyPI: Tracing the March 2026 TeamPCP supply chain campaign", "https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-teampcp-supply-chain-campaign/"],
            ]
        },
        {
            "heading": "UPCOMING EVENTS",
            "items": [
                ["Episode 4: The Network (Cellebrite)", "https://cellebrite.com/en/resources/webinars/the-network-episode-4/"],
                ["Episode 3: The Digital Trail (Cellebrite)", "https://cellebrite.com/en/resources/webinars/digital-trail-episode-3/"],
                ["Episode 2: The Insider (Cellebrite)", "https://cellebrite.com/en/resources/webinars/the-insider-episode-2/"],
                ["Episode 1: The First Red Flag (Cellebrite)", "https://cellebrite.com/en/resources/webinars/red-flag-episode-1/"],
                ["Bridging the air gap: Accelerating mobile forensics in secure, offline labs", "https://www.magnetforensics.com/resources/bridging-the-air-gap-accelerating-mobile-forensics-in-secure-offline-labs/"],
                ["Legal Unpacked S1:E6 // AI on trial: Understanding AI for lawyers", "https://www.magnetforensics.com/resources/legal-unpacked-s1e6-ai-on-trial-understanding-ai-for-lawyers/"],
                ["Stay Ahead of Ransomware – Initial Access via Evolving Social Engineering (SANS)", "https://www.sans.org/webcasts/stay-ahead-ransomware-initial-access/"],
            ]
        },
        {
            "heading": "PRESENTATIONS / PODCASTS",
            "items": [
                ["Beers with Talos breaks down the 2025 Talos Year in Review", "https://blog.talosintelligence.com/beers-with-talos-breaks-down-the-2025-talos-year-in-review/"],
                ["EP268 Weaponizing the Administrative Fabric: Cloud Identity and SaaS Compromise in M Trends 2026", "https://cloud.withgoogle.com/cloudsecurity/podcast/ep268-weaponizing-the-administrative-fabric-cloud-identity-and-saas-compromise-in-m-trends-2026/"],
                ["CQURE Hacks #76: Evading EDR Using Signed Driver", "https://cqureacademy.com/blog/cqure-hacks-76-evading-edr-using-signed-driver/"],
                ["Data vs Information vs Intelligence: A CTI Analyst's Guide", "https://kravensecurity.com/data-information-intelligence/"],
                ["Mobile Unpacked S4:E3 // Deducing the duplications: Understanding duplicated data in file systems", "https://www.magnetforensics.com/resources/s4e3-deducing-the-duplications-understanding-duplicated-data-in-file-systems/"],
                ["Winter SHIELD: Closing the Security Control Gap (Microsoft Threat Intelligence)", "https://thecyberwire.com/podcasts/microsoft-threat-intelligence/65/notes"],
                ["Regional Threats, Global Impact: A TA2725 Case Study (Proofpoint)", "https://www.buzzsprout.com/2445401/episodes/18912558-regional-threats-global-impact-a-ta2725-case-study.mp3"],
                ["Linux Password Hash Risks and Security Overview (Sandfly Security)", "https://sandflysecurity.com/blog/linux-password-hash-risks-and-security-overview"],
                ["Using GTI to Hunt Adversaries on the Dark Web (The Defender's Advantage)", "https://www.buzzsprout.com/1762840/episodes/18894011-using-gti-to-hunt-adversaries-on-the-dark-web.mp3"],
                ["Google's Cyber Disruption Unit; Coruna is Triangulation (Three Buddy Problem)", "http://securityconversations.fireside.fm/1"],
            ]
        },
        {
            "heading": "MALWARE",
            "items": [
                ["Kamasers Analysis: A Multi-Vector DDoS Botnet Targeting Organizations Worldwide", "https://any.run/cybersecurity-blog/kamasers-technical-analysis/"],
                ["Active Magecart Campaign Targets Spain, Steals Card Data via Hijacked eStores", "https://any.run/cybersecurity-blog/banks-magecart-campaign/"],
                ["Green Blood v2.0 ransomware analysis with decryption", "https://asec.ahnlab.com/en/92997/"],
                ["Illuminating VoidLink: Technical analysis of the VoidLink rootkit framework", "https://www.elastic.co/security-labs/illuminating-voidlink"],
                ["Elastic Security Labs uncovers BRUSHWORM and BRUSHLOGGER", "https://www.elastic.co/security-labs/brushworm-targets-financial-services"],
                ["When Malware Talks Back: Real-Time Interaction with a Threat Actor During the Analysis of Kiss Loader", "https://blog.gdatasoftware.com/2026/03/38399-analysis-kissloader"],
                ["Shellcode Analysis: Egg Hunters, Encoders, and Polymorphism", "https://infosecwriteups.com/shellcode-analysis-egg-hunters-encoders-and-polymorphism-e0cbb76c5871"],
                ["Infiniti Stealer: a new macOS infostealer using ClickFix and Python/Nuitka", "https://www.malwarebytes.com/blog/threat-intel/2026/03/infiniti-stealer-a-new-macos-infostealer-using-clickfix-and-python-nuitka"],
                ["GlassWorm attack installs fake browser extension for surveillance", "https://www.malwarebytes.com/blog/news/2026/03/glassworm-attack-installs-fake-browser-extension-for-surveillance"],
                ["Coruna: the framework used in Operation Triangulation", "https://securelist.com/coruna-framework-updated-operation-triangulation-exploit/119228/"],
                ["An AI gateway designed to steal your data", "https://securelist.com/litellm-supply-chain-attack/119257/"],
            ]
        },
        {
            "heading": "MISCELLANEOUS",
            "items": [
                ["Tips to Optimize DFIR Analysis Time in Belkasoft X", "https://belkasoft.com/dfir-analysis-time-optimization"],
                ["How Real-Time Evidence Sharing Helped the Orange County Sheriff's Office Solve a Florida Homicide", "https://cellebrite.com/en/resources/customer-stories/how-real-time-evidence-sharing-helped-the-orange-county-sheriffs-office-solve-a-florida-homicide/"],
                ["From Digital Investigations to Business Resilience: Key Private Sector Trends for 2026", "https://cellebrite.com/en/blog/digital-investigations-private-sector-trends-2026/"],
                ["Microsoft Defender for Office 365 Part 4: Anti-Spam & Anti-Malware", "https://cyberboo.substack.com/p/microsoft-defender-for-office-365-f99"],
                ["DFIR Jobs Update – 03/23/26", "https://dfirdominican.com/dfir-jobs-update-03-23-26/"],
                ["Entra — Finding App Name using deviceauth Endpoint", "https://diyinfosec.medium.com/entra-finding-app-name-using-deviceauth-endpoint-21f3e5ed0d94"],
                ["Security Automation with Elastic Workflows: From Alert to Response", "https://www.elastic.co/security-labs/security-automation-with-elastic-workflows/"],
                ["Distributed Password Recovery Goes 64-bit: Ready for RTX 5090", "https://blog.elcomsoft.com/2026/03/distributed-password-recovery-goes-64-bit-ready-for-rtx-5090/"],
                ["Arrested by AI", "https://blog.elcomsoft.com/2026/03/arrested-by-an-algorithm/"],
                ["Beyond Keywords: AI Classification For Forensic Email Review", "https://www.forensicfocus.com/articles/beyond-keywords-ai-classification-for-forensic-email-review/"],
                ["Digital Forensics Round-Up, March 25 2026", "https://www.forensicfocus.com/news/digital-forensics-round-up-march-25-2026/"],
                ["AI Email Classification Achieves 97.9% Accuracy—With No Training Phase Required", "https://www.forensicfocus.com/news/ai-email-classification-achieves-97-9-accuracy-with-no-training-phase-required/"],
                ["Defending with Microsoft: A Deep Dive into the Microsoft Defender Suite", "https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite/"],
                ["Book Review: 'Adverserial AI Attacks, Mitigations, and Defense Strategies'", "http://lockboxx.blogspot.com/2026/03/book-review-adverserial-ai-attacks.html"],
                ["Tool proliferation in DFIR: Why our toolkits keep growing", "https://www.magnetforensics.com/blog/tool-proliferation-in-dfir-why-our-toolkits-keep-growing-and-what-that-really-means/"],
                ["Bridging the air gap: Strengthening mobile workflows with Graykey Fastrak", "https://www.magnetforensics.com/blog/bridging-the-air-gap-strengthening-mobile-workflows-with-graykey-fastrak-and-axiom-express-extraction/"],
                ["Oxygen Remote Explorer vs. Oxygen Forensic® Detective: Choosing the right platform", "https://www.oxygenforensics.com/resources/oxygen-remote-explorer-vs-oxygen-forensic-detective/"],
                ["Building a Firewall …via Endpoint Security!? (Patrick Wardle)", "https://objective-see.org/blog/blog_0x86.html"],
                ["Mandiant Global Median Dwell Time Deteriorates from 11 to 14 Days", "https://taosecurity.blogspot.com/2026/03/mandiant-global-median-dwell-time.html"],
                ["Why 47? The Math Behind 'AI Attacks 47x Faster Than Humans'", "https://robtlee73.substack.com/p/why-47-the-math-behind-ai-attacks"],
                ["The Port Scoping Paradox: When Optimization Makes Things Slower", "http://travisgreen.net/2026/02/12/port-scoping-paradox.html"],
                ["England Police Rugby Set For Argentina And Uruguay Tour With Detego Global", "https://www.forensicfocus.com/news/england-police-rugby-set-for-argentina-and-uruguay-tour-with-detego-global-as-main-sponsor/"],
            ]
        },
        {
            "heading": "SOFTWARE UPDATES",
            "items": [
                ["25G Fiber extension + TaskForce 2026.2 update (Atola)", "https://blog.atola.com/25g-fiber-tf-2026-2/"],
                ["Amped Replay Update 40205: Magnify and Spotlight Improvements", "https://blog.ampedsoftware.com/2026/03/25/amped-replay-update-40205"],
                ["23 March 2026: Apache Tika Release", "https://tika.apache.org/"],
                ["Browser History Examiner Version 1.23.2 – March 27, 2026", "https://www.foxtonforensics.com/browser-history-examiner/version-history"],
                ["FalconPy Version 1.6.1", "https://github.com/CrowdStrike/falconpy/releases/tag/v1.6.1"],
                ["Elcomsoft Distributed Password Recovery goes 64-bit, adds NVIDIA Blackwell support", "https://www.elcomsoft.com/news/876.html"],
                ["Crow-Eye v0.8.0", "https://github.com/Ghassan-elsman/Crow-Eye/releases/tag/v0.8.0"],
                ["Timesketch 20260326", "https://github.com/google/timesketch/releases/tag/20260326"],
                ["Announcing ida-mcp 2.0: A Headless MCP Server for IDA Pro", "https://jtsylve.blog/post/2026/03/25/Announcing-ida-mcp-2"],
                ["Q1 2026 Major Release is now available (MSAB)", "https://www.msab.com/updates/q1-2026-major-release-is-now-available/"],
                ["OpenCTI 7.260326.0", "https://github.com/OpenCTI-Platform/opencti/releases/tag/7.260326.0"],
                ["Sandfly 5.7 – Performance Upgrade", "https://sandflysecurity.com/blog/sandfly-57-performance-upgrade"],
                ["IPED 4.3.1", "https://github.com/sepinf-inc/IPED/releases/tag/4.3.1"],
                ["RECON ITR Version 26.0.0", "https://sumuri.com/recon-itr-release-notes/"],
                ["uac-3.3.0-rc1", "https://github.com/tclahr/uac/releases/tag/v3.3.0-rc1"],
                ["X-Ways Forensics 21.8 Preview 5", "https://www.x-ways.net/winhex/forum/messages/1/5537.html"],
            ]
        },
    ]
}

# ─── WEEK 12 DATA (2026-03-22) ────────────────────────────────────────────────
W_PREV1 = {
    "name": "22 March 2026",
    "date": "This Week in 4n6",
    "url": "https://thisweekin4n6.com/2026/03/22/week-12-2026/",
    "sections": [
        {
            "heading": "FORENSIC ANALYSIS",
            "items": [
                ["AI-Powered Picture Analysis with BelkaGPT", "https://belkasoft.com/ai-powered-picture-analysis"],
                ["Looks Can Lie: Is That Really an NVMe Drive?", "https://blog.elcomsoft.com/2026/03/looks-can-lie-is-that-really-an-nvme-drive/"],
                ["2026 MSAB CTF: Android Questions", "https://www.hexordia.com/blog/2026-msab-ctf-android-questions"],
                ["2026 MSAB CTF: iOS Questions", "https://www.hexordia.com/blog/2026-msab-ctf-ios-questions"],
                ["BDC – More Battery Temps & Charging Stats for iOS", "https://www.stark4n6.com/2026/03/bdc-more-battery-temps-charging-stats.html"],
                ["Tracking LockBit Through Memory Forensics", "https://systemweakness.com/tracking-lockbit-through-memory-forensics-a0ba37aba21c"],
            ]
        },
        {
            "heading": "THREAT INTELLIGENCE / HUNTING",
            "items": [
                ["CVE-2025-32975: Arctic Wolf Observes Exploitation of Quest KACE Systems Management Appliance", "https://arcticwolf.com/resources/blog-uk/cve-2025-32975-arctic-wolf-observes-exploitation-of-quest-kace-systems-management-appliance/"],
                ["Nation-State Attacks Hit Machine Speed: Key Takeaways of the 2026 Armis Cyberwarfare Report", "https://www.armis.com/blog/nation-state-attacks-hit-machine-speed-key-takeaways-of-the-2026-armis-cyberwarfare-report-and-what-it-means-for-security-teams/"],
                ["February 2026 APT Attack Trends Report (South Korea)", "https://asec.ahnlab.com/en/92972/"],
                ["Winos4.0 malware disguised as KakaoTalk installation file", "https://asec.ahnlab.com/en/92971/"],
                ["Attack case against MS-SQL server installing ICE Cloud scanner", "https://asec.ahnlab.com/en/92988/"],
                ["From flat networks to locked up domains with tiering models", "https://sensepost.com/blog/2026/from-flat-networks-to-locked-up-domains-with-tiering-models/"],
                ["LotAI: How Attackers Weaponize AI Assistants for Data Exfiltration", "https://www.blackfog.com/lotai-weaponizing-ai-tools-for-data-exfiltration/"],
                ["2026-03-12: Files for an ISC diary (SmartApeSG ClickFix pushes Remcos RAT)", "https://www.malware-traffic-analysis.net/2026/03/12/index.html"],
                ["Feds Disrupt IoT Botnets Behind Huge DDoS Attacks", "https://krebsonsecurity.com/2026/03/feds-disrupt-iot-botnets-behind-huge-ddos-attacks/"],
                ["NetSupport Manager: Tracking Dual-Use Remote Administration Infrastructure", "https://censys.com/blog/netsupport-manager-tracking-dual-use-remote-administration-infrastructure/"],
                ["Hunting Cameras in the Dark: Finding Internet Cameras Before Adversaries Do", "https://censys.com/blog/blog-finding-internet-cameras-before-adversaries-do/"],
                ["ResidentBat: Belarusian KGB Android Spyware at Internet Scale", "https://censys.com/blog/residentbat-belarusian-kgb-spyware/"],
                ["16th March – Threat Intelligence Report (Check Point)", "https://research.checkpoint.com/2026/16th-march-threat-intelligence-report/"],
                ["Transparent COM instrumentation for malware analysis (Cisco Talos)", "https://blog.talosintelligence.com/transparent-com-instrumentation-for-malware-analysis/"],
                ["Everyday tools, extraordinary crimes: the ransomware exfiltration playbook", "https://blog.talosintelligence.com/everyday-tools-extraordinary-crimes-the-ransomware-exfiltration-playbook/"],
                ["MacSync Stealer: SEO Poisoning and ClickFix-Based macOS Malware Delivery Chain", "https://www.cloudsek.com/blog/macsync-stealer-seo-poisoning-and-clickfix-based-macos-malware-delivery-chain"],
                ["LiveChat Abuse: How Phishers Are Exploiting SaaS Support Tools to Steal Sensitive Data", "https://cofense.com/blog/livechat-phishing-abuse/"],
                ["Weekly Threat Infrastructure Investigation (Week 9,10)", "https://disconinja.hatenablog.com/entry/2026/03/17/215616"],
                ["Microsoft Graph API Attack Surface: OAuth Flows, Abused Endpoints", "https://infosecwriteups.com/microsoft-graph-api-attack-surface-oauth-flows-abused-endpoints-and-what-defenders-miss-9c303ea2aa02"],
                ["New Malware Highlights Increased Systematic Targeting of Network Infrastructure", "https://eclypsium.com/blog/condibot-monaco-malware-network-infrastructure/"],
                ["Linux & Cloud Detection Engineering – Getting Started with Defend for Containers (D4C)", "https://www.elastic.co/security-labs/getting-started-with-defend-for-containers"],
                ["Linux & Cloud Detection Engineering – TeamPCP Container Attack Scenario", "https://www.elastic.co/security-labs/teampcp-container-attack-scenario"],
                ["WIPED IN 79 COUNTRIES: The Handala Hack Attack on Stryker Corporation", "https://falconfeeds.io/blogs/handala-hack-attack-on-stryker-corporation"],
                ["DLL Search Order Hijacking: Finding and Exploiting the Flaw", "https://infosecwriteups.com/dll-search-order-hijacking-finding-and-exploiting-the-flaw-9f5dabaa2470"],
                ["CTI Research: MuddyWater/Seedworm (Mango Sandstorm)", "https://infosecwriteups.com/cti-research-muddywater-seedworm-mango-sandstorm-ebf6af5ba061"],
            ]
        },
        {
            "heading": "UPCOMING EVENTS",
            "items": [
                ["BHIS – Talkin' Bout [infosec] News 2026-03-23", "https://www.bhis.com/talkin-bout-infosec-news-2026-03-23/"],
                ["Advanced Digital Investigations in Africa: Unlocking the Evidence Hidden in Every Device (Cellebrite)", "https://cellebrite.com/en/resources/webinars/advanced-digital-investigations-in-africa-unlocking-the-evidence-hidden-in-every-device/"],
                ["Investigating Evasion: How to Find What the Alert Missed", "https://register.gotowebinar.com/register/9096089726229071963"],
                ["Mobile Unpacked S4:E3 // Deducing the duplications: Understanding duplicated data in file systems", "https://www.magnetforensics.com/resources/s4e3-deducing-the-duplications-understanding-duplicated-data-in-file-systems/"],
                ["2026 Threat Landscape: Turning Threat Intelligence into Analytic Advantage", "https://www.linkedin.com/events/7438173815626641409/"],
            ]
        },
        {
            "heading": "PRESENTATIONS / PODCASTS",
            "items": [
                ["Signals in the noise: Five years of enterprise DFIR trends", "https://www.magnetforensics.com/resources/the-state-of-enterprise-dfir-2026-how-ai-collaboration-and-integration-are-redefining-digital-investigations/"],
                ["Bridging the air gap: Accelerating mobile forensics in secure, offline labs", "https://www.magnetforensics.com/resources/bridging-the-air-gap-accelerating-mobile-forensics-in-secure-offline-labs/"],
            ]
        },
        {
            "heading": "MALWARE",
            "items": [
                ["Glassworm Strikes Popular React Native Phone Number Packages", "https://www.aikido.dev/blog/glassworm-strikes-react-packages-phone-numbers"],
                ["fast-draft Open VSX Extension Compromised by BlokTrooper", "https://www.aikido.dev/blog/fast-draft-open-vsx-bloktrooper"],
                ["GlassWorm Hides a RAT Inside a Malicious Chrome Extension", "https://www.aikido.dev/blog/glassworm-chrome-extension-rat"],
                ["TeamPCP deploys CanisterWorm on NPM following Trivy compromise", "https://www.aikido.dev/blog/teampcp-deploys-worm-npm-trivy-compromise"],
                ["Forbidden Hyena adopts BlackReaperRAT in AI-powered campaigns", "https://bi-zone.medium.com/forbidden-hyena-adopts-blackreaperrat-in-ai-powered-campaigns-26aa61dff896"],
                ["Windsurf IDE Extension Drops Malware via Solana Blockchain", "https://www.bitdefender.com/en-us/blog/labs/windsurf-extension-malware-solana"],
                ["OpenClaw Developers Targeted in Crypto-Wallet Phishing Attack", "https://www.ox.security/blog/openclaw-github-phishing-crypto-wallet-attack/"],
                ["Free real estate: GoPix, the banking Trojan living off your memory", "https://securelist.com/gopix-banking-trojan/119173/"],
                ["The SOC Files: Time to 'Sapecar'. Unpacking a new Horabot campaign in Mexico", "https://securelist.com/horabot-campaign/119033/"],
                ["Operation GhostMail: Russian APT exploits Zimbra Webmail to Target Ukraine State Agency", "https://www.seqrite.com/blog/operation-ghostmail-zimbra-xss-russian-apt-ukraine/"],
                ["Analysis of Batch File leads to DonutLoader", "https://medium.com/@shubhandrew/analysis-of-batch-file-leads-to-donutloader-a18705e9a007"],
                ["Beyond the Wiper — What Unit42's Iran Analysis Misses", "https://plausible-deniability.co/blog/BeyondWiper/"],
                ["Nothing but dotnet when we shoot", "https://plausible-deniability.co/blog/Nothing-but-dotnet-when-we-shoot/"],
            ]
        },
        {
            "heading": "MISCELLANEOUS",
            "items": [
                ["Introducing DFIR Toolkit: Privacy-First DFIR utilities that run entirely in your browser", "https://andreafortuna.org/2026/03/17/dfir-toolkit.html"],
                ["If you suck at your DFIR job, AI is going to take it.", "https://brettshavers.com/brett-s-blog/entry/if-you-suck-at-your-dfir-job-ai-is-going-to-take-it"],
                ["A Practical Map of the DFIR Internet: Marketplaces, FAQs, and Fire Exits", "https://www.dfir.training/blog/a-practical-map-of-the-dfir-internet-marketplaces-faqs-and-fire-exits"],
                ["56% are either likely to leave DFIR within 12 months or unsure if they'll stay", "https://www.dfir.training/blog/56-of-dfir-is-unsure-if-they-will-stay-in-dfir-for-the-next-12-months"],
                ["Cellebrite Changes the Investigative Game with the Launch of Genesis, Agentic AI for Digital Investigations", "https://cellebrite.com/en/resources/press-releases/cellebrite-launches-genesis-agentic-ai-for-digital-investigations-cellebrite/"],
                ["JeongKyun Park, Information Security Student And Independent Developer, Korea Cyber University", "https://www.forensicfocus.com/interviews/jeongkyun-park-information-security-student-and-independent-developer-korea-cyber-university/"],
                ["Digital Forensics Round-Up, March 18 2026", "https://www.forensicfocus.com/news/digital-forensics-round-up-march-18-2026/"],
                ["Rob Fried On New Challenges In Digital Forensics (Podcast)", "https://www.forensicfocus.com/podcast/rob-fried-on-new-challenges-in-digital-forensics/"],
                ["Forensic Focus Digest, March 20 2026", "https://www.forensicfocus.com/news/forensic-focus-digest-march-20-2026/"],
                ["Explainer: Disk images (Howard Oakley, eclectic light)", "https://eclecticlight.co/2026/03/21/explainer-disk-images/"],
                ["Upcoming Webinar – Mastering Triage: Intro To ADF Pro", "https://www.forensicfocus.com/news/upcoming-webinar-mastering-triage-intro-to-adf-pro/"],
                ["Introducing Aid4Mail: Closing Email Evidence Gaps for Investigators", "https://www.forensicfocus.com/news/introducing-aid4mail-closing-email-evidence-gaps-for-investigators/"],
            ]
        },
        {
            "heading": "SOFTWARE UPDATES",
            "items": [
                ["Malwoverview 8.0.0", "https://github.com/alexandreborges/malwoverview/releases/tag/v8.0.0"],
                ["Arkime v6.1.0", "https://github.com/arkime/arkime/releases/tag/v6.1.0"],
                ["From Enumeration to Findings: The Security Findings Report in EntraFalcon", "https://blog.compass-security.com/2026/03/from-enumeration-to-findings-the-security-findings-report-in-entrafalcon/"],
                ["oledump.py Version 0.0.85 (Didier Stevens)", "https://blog.didierstevens.com/2026/03/17/update-oledump-py-version-0-0-85/"],
                ["winfor-salt v2026.5.4", "https://github.com/digitalsleuth/winfor-salt/releases/tag/v2026.5.4"],
                ["VolWeb v3.16.0", "https://github.com/k1nd0ne/VolWeb/releases/tag/v3.16.0"],
                ["Arc2Lite v2.0.0 – Combined Script", "https://github.com/stark4n6/Arc2Lite/releases/tag/v2.0.0"],
                ["MacOS-Analyzer-Suite v1.2.0", "https://github.com/LETHAL-FORENSICS/MacOS-Analyzer-Suite/releases/tag/v1.2.0"],
                ["AD_Miner v1.9.0", "https://github.com/AD-Security/AD_Miner/releases/tag/v1.9.0"],
                ["MISP-STIX 2026.3.13 Released", "https://www.misp-project.org/2026/03/13/misp-stix-2026-3-13-released/"],
                ["MISP 2.4.205 Released", "https://www.misp-project.org/2026/03/17/misp-2-4-205-released/"],
                ["OpenCTI 6.9.26", "https://github.com/OpenCTI-Platform/opencti/releases/tag/6.9.26"],
                ["Security Onion 2.4.210 Released", "https://blog.securityonion.net/2026/03/security-onion-24210-released/"],
                ["YARA-X 1.3.0", "https://github.com/VirusTotal/yara-x/releases/tag/v1.3.0"],
                ["KMLer: a CSV / XLSX to KML Tool", "https://metadataperspective.com/2026/03/13/kmler-a-csv-xlsx-to-kml-tool/"],
            ]
        },
    ]
}

# ─── WEEK 11 DATA (2026-03-15) ────────────────────────────────────────────────
W_PREV2 = {
    "name": "15 March 2026",
    "date": "This Week in 4n6",
    "url": "https://thisweekin4n6.com/2026/03/15/week-11-2026/",
    "sections": [
        {
            "heading": "FORENSIC ANALYSIS",
            "items": [
                ["Deep‑Dive Forense in Box per iOS (Django Faiola)", "https://djangofaiola.blogspot.com/2026/03/deepdive-forense-in-box-per-ios.html"],
                ["The C:\\User Data in Windows Forensics", "https://blog.elcomsoft.com/2026/03/the-cuser-data-in-windows-forensics/"],
                ["Android Pre-Installed Apps: What Could Possibly Go Wrong?", "https://blog.elcomsoft.com/2026/03/android-pre-installed-apps-what-could-possibly-go-wrong/"],
                ["Apple Spotlight (ForensAFE)", "https://forensafe.com/blogs/apple-spotlight.html"],
                ["From Chaos to Chronology: The Power of Forensic Timelines", "https://www.thedfirspot.com/post/from-chaos-to-chronology-the-power-of-forensic-timelines"],
            ]
        },
        {
            "heading": "THREAT INTELLIGENCE / HUNTING",
            "items": [
                ["Glassworm Is Back: A New Wave of Invisible Unicode Attacks Hits Hundreds of Repositories", "https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode"],
                ["Google Cloud Security Threat Horizons Report #13 (H1 2026)", "https://medium.com/anton-on-security/google-cloud-security-threat-horizons-report-13-h1-2026-is-out-926df5bb72a1"],
                ["Kernel in the Crosshairs: The BlackSanta Threat Campaign Targeting Recruitment Workflows", "https://www.aryaka.com/blog/kernel-in-the-crosshairs-blacksanta-edr-killer-recruitment-workflows/"],
                ["Defending Against Iranian Cyber Threats in the Wake of Operation Epic Fury", "https://www.attackiq.com/2026/03/05/operation-epic-fury/"],
                ["Windows and macOS Malware Spreads via Fake 'Claude Code' Google Ads", "https://www.bitdefender.com/en-us/blog/labs/fake-claude-code-google-ads-malware"],
                ["NetSupport RAT: How Legitimate Tools Can Be as Damaging as Malware", "https://www.darktrace.com/blog/netsupport-rat-how-legitimate-tools-can-be-as-damaging-as-malware"],
                ["Behind the console: Active phishing campaign targeting AWS console credentials", "https://securitylabs.datadoghq.com/articles/behind-the-console-aws-aitm-phishing-campaign/"],
                ["The Red Queen's Race: Arms Race Dynamics in Threat Detection", "https://detect.fyi/the-red-queens-race-arms-race-dynamics-in-threat-detection-4f532a149fda"],
                ["Beyond the IP: Identifying Compromised Identities in RDP Sessions", "https://detect.fyi/beyond-the-ip-identifying-compromised-identities-in-rdp-sessions-98ce6931d73f"],
                ["Phishing EasyPark: il brand sfruttato per sottrarre dati di pagamento", "https://www.d3lab.net/phishing-easypark-il-brand-sfruttato-per-sottrarre-dati-di-pagamento-e-documenti-di-identita/"],
                ["The Invisible Architecture of Modern Phishing", "https://www.invictus-ir.com/news/the-invisible-architecture-of-modern-phishing"],
                ["Silence of the hops: The KadNap botnet", "https://blog.lumen.com/silence-of-the-hops-the-kadnap-botnet/"],
                ["Fake Temu Coin airdrop uses ClickFix trick to install stealthy malware", "https://www.malwarebytes.com/blog/threat-intel/2026/03/fake-temu-coin-airdrop-uses-clickfix-trick-to-install-stealthy-malware"],
                ["Contagious Interview: Malware delivered through fake developer job interviews", "https://www.microsoft.com/en-us/security/blog/2026/03/11/contagious-interview-malware-delivered-through-fake-developer-job-interviews/"],
                ["Storm-2561 uses SEO poisoning to distribute fake VPN clients for credential theft", "https://www.microsoft.com/en-us/security/blog/2026/03/12/storm-2561-uses-seo-poisoning-to-distribute-fake-vpn-clients-for-credential-theft/"],
                ["T1059.012 Hypervisor CLI in MITRE ATT&CK Explained", "https://www.picussecurity.com/resource/blog/t1059-012-hypervisor-cli"],
                ["When Proxies Become the Attack Vectors in Web Architectures", "https://www.praetorian.com/blog/cve-2026-0953-bypass-tutor-lms-pro-auth-vulnerability/"],
                ["Et Tu, RDP? Detecting Sticky Keys Backdoors with Brutus and WebAssembly", "https://www.praetorian.com/blog/rdp-sticky-keys-backdoor-brutus/"],
                ["Iran conflict drives heightened espionage activity against Middle East targets", "https://www.proofpoint.com/us/blog/threat-insight/iran-conflict-drives-heightened-espionage-activity-against-middle-east-targets"],
                ["Rapid7 Detection Coverage for Iran-Linked Cyber Activity", "https://www.rapid7.com/blog/post/tr-detection-coverage-iran-linked-cyber-activity/"],
                ["Iran's Cyber Playbook in the Escalating Regional Conflict", "https://www.rapid7.com/blog/post/tr-iran-cyber-playbook-escalating-regional-conflict/"],
                ["73 Malicious Open VSX Extensions Linked to GlassWorm Campaign Now Using Transitive Dependencies", "https://socket.dev/blog/open-vsx-transitive-glassworm-campaign"],
                ["Dark Web Profile: Handala Hack", "https://socradar.io/blog/dark-web-profile-handala-hack/"],
                ["Evil evolution: ClickFix and macOS infostealers", "https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers"],
                ["Initial access techniques used by Iran-based threat actors", "https://www.sophos.com/en-us/blog/initial-access-techniques-used-by-iran-based-threat-actors"],
            ]
        },
        {
            "heading": "UPCOMING EVENTS",
            "items": [
                ["Do it, do it NOW! – A Pre-Incident Checklist w/ Patterson (BHIS)", "https://www.bhis.com/pre-incident-checklist-patterson/"],
                ["BHIS – Talkin' Bout [infosec] News 2026-03-16", "https://www.bhis.com/talkin-bout-infosec-news-2026-03-16/"],
                ["Building the Force of the Future: People, Culture, and the Road to 2030 (Cellebrite)", "https://cellebrite.com/en/resources/webinars/building-the-force-of-the-future-people-culture-and-the-road-to-2030/"],
                ["Investigate at the Speed of Now: AI, Automation, and the Modern Workflow (Cellebrite)", "https://cellebrite.com/en/resources/webinars/investigate-at-the-speed-of-now-ai-automation-and-the-modern-workflow/"],
                ["The New Crime Scene: Intelligence, Data, and the Cloud Advantage (Cellebrite)", "https://cellebrite.com/en/resources/webinars/the-new-crime-scene-intelligence-data-and-the-cloud-advantage/"],
                ["Digital Policing 2030: How Artificial Intelligence is Reshaping Law Enforcement (Cellebrite)", "https://cellebrite.com/en/resources/webinars/digital-policing-2030-how-artificial-intelligence-is-reshaping-law-enforcement/"],
                ["Signals in the noise: Five years of enterprise DFIR trends (Magnet)", "https://www.magnetforensics.com/resources/the-state-of-enterprise-dfir-2026-how-ai-collaboration-and-integration-are-redefining-digital-investigations/"],
                ["2026 Industry Trends: How Digital Forensics Is Redefining Public Safety (Forensic Focus Webinar)", "https://www.forensicfocus.com/news/upcoming-webinar-2026-industry-trends/"],
                ["SANS: Forensics and Incident Response courses 2026", "https://www.sans.org/dfir/"],
            ]
        },
        {
            "heading": "PRESENTATIONS / PODCASTS",
            "items": [
                ["Breaking Down the New National Cybersecurity Strategy (CrowdStrike)", "https://crowdstrike.podbean.com/e/breaking-down-the-new-national-cybersecurity-strategy/"],
                ["EP266 Resetting the SOC for Code War: Allie Mellen on Detecting State Actors (Google Cloud Security)", "https://cloud.withgoogle.com/cloudsecurity/podcast/ep266-resetting-the-soc-for-code-war-allie-mellen-on-detecting-state-actors-vs-doing-the-basics/"],
                ["The Game Is Afoot: Introducing the MalChela Video Series", "https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/"],
                ["Protecting your organization from manipulated media with Magnet Verify", "https://www.magnetforensics.com/resources/protecting-your-organization-from-manipulated-media-with-magnet-verify/"],
                ["A unified workflow for modern CSAM investigations (Magnet)", "https://www.magnetforensics.com/resources/a-unified-workflow-for-modern-csam-investigations/"],
                ["AI as Tradecraft: How Threat Actors Are Operationalizing AI (Microsoft Threat Intelligence)", "https://thecyberwire.com/podcasts/microsoft-threat-intelligence/64/notes"],
            ]
        },
        {
            "heading": "MALWARE",
            "items": [
                ["MicroStealer Analysis: A Fast-Spreading Infostealer with Limited Detection", "https://any.run/cybersecurity-blog/microstealer-technical-analysis/"],
                ["February 2026 Infostealer Trend Report", "https://asec.ahnlab.com/en/92902/"],
                ["February 2026 APT Group Trends Report", "https://asec.ahnlab.com/en/92906/"],
                ["February 2026 Phishing Email Trends Report", "https://asec.ahnlab.com/en/92907/"],
                ["MuddyWater APT + Tsundere Botnet: EtherHiding the C2", "https://www.esentire.com/blog/muddywater-apt-tsundere-botnet-etherhiding-the-c2"],
                ["Endgame Harvesting: Inside ACRStealer's Modern Infrastructure", "https://blog.gdatasoftware.com/2026/03/38385-acr-stealer-infrastructure"],
                ["PE Import Analyzer: A Practical Guide for Malware Analysts and Reverse Engineers", "https://infosecwriteups.com/pe-import-analyzer-a-practical-guide-for-malware-analysts-and-reverse-engineers-29b8b98aeaf3"],
                ["Unpacker: A Practical Guide to Modular Malware Packer Detection and Unpacking", "https://infosecwriteups.com/unpacker-a-practical-guide-to-modular-malware-packer-detection"],
                ["DroidBot: The Android Banking Trojan That Learns From Victims", "https://www.kaspersky.com/blog/droidbot-android-banking-trojan/"],
                ["XenoRAT Disguised As a Legitimate Utility", "https://www.malwarebytes.com/blog/threat-intel/2026/03/xenorat-disguised-as-legitimate-utility/"],
                ["New Python-Based Malware Targets Linux Systems via Cron Jobs", "https://securelist.com/python-linux-malware-cron-jobs/119050/"],
                ["RustyAttr Trojan — macOS Malware Masquerading as Extended Attributes", "https://www.sentinelone.com/blog/rustyattr-trojan-macos-malware/"],
                ["StealBit, LockBit's Custom Data-Theft Tool, Re-emerges", "https://www.trellix.com/blogs/research/stealbit-lockbit-custom-data-theft/"],
                ["Malware-As-A-Service Redefined: Why XWorm is outpacing every other RAT", "https://www.trellix.com/blogs/research/malware-as-a-service-redefined-xworm-rat/"],
                ["New Malware Campaign Leverages Windows Installer for Lateral Movement", "https://www.trendmicro.com/en_us/research/26/c/windows-installer-lateral-movement.html"],
            ]
        },
        {
            "heading": "MISCELLANEOUS",
            "items": [
                ["Microsoft Defender for Office 365 Part 2: Deployment & Configuration Guide", "https://cyberboo.substack.com/p/microsoft-defender-for-office-365-4b8"],
                ["Microsoft Defender for Office 365 Part 3: Email Authentication Deep Dive", "https://cyberboo.substack.com/p/microsoft-defender-for-office-365-email-authentication-deep-dive"],
                ["DFIR Jobs Update – 03/09/26", "https://dfirdominican.com/dfir-jobs-update-03-09-26/"],
                ["Emma Pickering, Head Of Technology-Facilitated Abuse And Economic Empowerment, Refuge (Forensic Focus Interview)", "https://www.forensicfocus.com/interviews/emma-pickering-head-of-technology-facilitated-abuse-and-economic-empowerment-refuge/"],
                ["Forensics Europe Expo Returns To London In July 2026", "https://www.forensicfocus.com/news/forensics-europe-expo-returns-to-london-in-july-2026/"],
                ["Yuri Gubanov, Founder And CEO, Belkasoft (Forensic Focus Interview)", "https://www.forensicfocus.com/interviews/yuri-gubanov-founder-and-ceo-belkasoft/"],
                ["Upcoming Webinar – 2026 Industry Trends: How Digital Forensics Is Redefining Public Safety", "https://www.forensicfocus.com/news/upcoming-webinar-mastering-triage-intro-to-adf-pro/"],
                ["Odd Lots: Cyberwar in the Age of AI", "https://www.msuiche.com/posts/odd-lots-cyberwar-in-the-age-of-ai/"],
                ["Digital Forensics Round-Up, March 11 2026", "https://www.forensicfocus.com/news/digital-forensics-round-up-march-11-2026/"],
                ["Forensic Focus Digest, March 13 2026", "https://www.forensicfocus.com/news/forensic-focus-digest-march-13-2026/"],
                ["Microsoft Ownerless Agents: The silent risk in your Entra tenant", "https://thalpius.com/2026/03/microsoft-ownerless-agents-the-silent-risk/"],
                ["Explainer: Disk images (macOS)", "https://eclecticlight.co/2026/03/14/explainer-disk-images/"],
            ]
        },
        {
            "heading": "SOFTWARE UPDATES",
            "items": [
                ["Malwoverview 7.1.2", "https://github.com/alexandreborges/malwoverview/releases/tag/v7.1.2"],
                ["Amped Authenticate Update 40074: Faster and Updated Deepfake Detection", "https://blog.ampedsoftware.com/2026/03/11/authenticate-update-40074"],
                ["Arkime v6.0.1", "https://github.com/arkime/arkime/releases/tag/v6.0.1"],
                ["emldump.py Version 0.0.16 (Didier Stevens)", "https://blog.didierstevens.com/2026/03/09/update-emldump-py-version-0-0-16/"],
                ["search-for-compression.py 0.0.6 (Didier Stevens)", "https://blog.didierstevens.com/2026/03/10/update-search-for-compression-py-0-0-6/"],
                ["pecheck.py Version 0.7.20 (Didier Stevens)", "https://blog.didierstevens.com/2026/03/11/update-pecheck-py-version-0-7-20/"],
                ["zipdump.py Version 0.0.34 (Didier Stevens)", "https://blog.didierstevens.com/2026/03/12/update-zipdump-py-version-0-0-34-2/"],
                ["pdf-parser.py Version 0.7.14 (Didier Stevens)", "https://blog.didierstevens.com/2026/03/13/update-pdf-parser-py-version-0-7-14/"],
                ["xLEAPP – Helper scripts for pulling/cloning and creation of Windows exe", "https://bebinary4n6.blogspot.com/2026/03/xleapp-helper-scripts-for.html"],
                ["Bubbly now with GUI – New Release 1.2.4", "https://bebinary4n6.blogspot.com/2026/03/bubbly-now-with-gui-new-release-124.html"],
                ["MISP Workbench v1.0 (beta) Released", "https://www.misp-project.org/2026/03/13/misp-workbench_beta_1.0_released.html/"],
                ["Fetch v5.2 (North Loop Consulting)", "https://northloopconsulting.com/blog/f/fetch-v52"],
                ["OpenCTI 6.9.26", "https://github.com/OpenCTI-Platform/opencti/releases/tag/6.9.26"],
                ["Security Onion 2.4.211 Is Now Available", "https://blog.securityonion.net/2026/03/security-onion-24211-is-now-available.html"],
                ["pySigma v1.2.0", "https://github.com/SigmaHQ/pySigma/releases/tag/v1.2.0"],
                ["KMLer: a CSV / XLSX to KML Tool", "https://metadataperspective.com/2026/03/13/kmler-a-csv-xlsx-to-kml-tool/"],
                ["LevelDB Recon v1.0.0.53", "https://x.com/ArsenalRecon/status/2030997920107884668"],
            ]
        },
    ]
}

# ─── START.ME FEED ITEMS ─────────────────────────────────────────────────────
STARTME_ITEMS = [
    ["Impacket for Pentester: DACLEdit", "https://www.hackingarticles.in/impacket-for-pentester-dacledit/"],
    ["29 March 2026 (This Week in 4n6)", "https://thisweekin4n6.com/2026/03/29/week-13-2026/"],
    ["The Linux Concept Journey — Extended File Attributes (xattr)", "https://medium.com/@boutnaru/the-linux-concept-journey-extended-file-attributes-xattr-179daa4f1b92"],
    ["iOS Lockdown mode and forensic analysis: a technical perspective", "https://andreafortuna.org/2026/03/29/ios-lockdown-mode-forensics/"],
    ["The Linux Security Journey — nosuid (No Set UID) File System Support", "https://medium.com/@boutnaru/the-linux-security-journey-nosuid-no-set-uid-file-system-support-7eb042c1dcbd"],
    ["Bloomin' Biomes - Meet Sedgwick (North Loop Consulting)", "https://northloopconsulting.com/blog/f/bloomin-biomes---meet-sedgwick"],
    ["System Configuration: File Shares & Offline Caching", "https://medium.com/@cyberengage.org/system-configuration-file-shares-offline-caching-e0ad9096b3a7"],
    ["Episode 4: The Network (Cellebrite)", "https://cellebrite.com/en/resources/webinars/the-network-episode-4/"],
    ["Episode 3: The Digital Trail (Cellebrite)", "https://cellebrite.com/en/resources/webinars/digital-trail-episode-3/"],
    ["Episode 2: The Insider (Cellebrite)", "https://cellebrite.com/en/resources/webinars/the-insider-episode-2/"],
    ["Episode 1: The First Red Flag (Cellebrite)", "https://cellebrite.com/en/resources/webinars/red-flag-episode-1/"],
    ["A Detection Researcher Mindset — DCSYNC T1003.006", "https://detect.fyi/a-detection-researcher-mindset-dcsync-t1003-006-2532bddefbf5"],
    ["A Detection Researcher Mindset", "https://detect.fyi/a-detection-researcher-mindset-f2ed045480c5"],
    ["Thesis Friday #20: Project Stark – Forensic Reconstruction of the CarPlay Handshake", "https://startme.stark4n6.com/thesis-friday-20"],
    ["From Digital Investigations to Business Resilience: Key Private Sector Trends for 2026", "https://cellebrite.com/en/blog/digital-investigations-private-sector-trends-2026/"],
    ["Arrested by AI (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/arrested-by-an-algorithm/"],
    ["The Windows Security Journey — RDP Public Mode", "https://medium.com/@boutnaru/the-windows-security-journey-rdp-public-mode"],
    ["Linux Forensic Scenario (Righteous IT)", "https://righteousit.com/2026/03/27/linux-forensic-scenario/"],
    ["Ghost in LSASS: Detecting KslKatz Credential Dumping Framework", "https://detect.fyi/ghost-in-lsass-detecting-kslkatz-credential-dumping-framework-8645f246aec9"],
    ["ShellBags and User Navigation: What Windows Remembers About Exploration", "https://sethenoka.com/shellbags-and-user-navigation-what-windows-remembers-about-exploration/"],
]

# ─── BRUTALIST REPORT ITEMS ──────────────────────────────────────────────────
BRUTALIST_ITEMS = [
    ["Stripe withheld $85,000 from our EU platform – no legal basis given", "https://news.ycombinator.com/item?id=stripe-eu"],
    ["C++26 is done — ISO C++ standards meeting, Trip Report", "https://herbsutter.com/2026/03/29/c26-is-done-trip-report-march-2026-iso-c-standards-meeting-london-croydon-uk/"],
    ["Neovim 0.12.0 Released", "https://github.com/neovim/neovim/releases/tag/v0.12.0"],
    ["First Western Digital, now Sony: The tech giant suspends SD card sales", "https://mashable.com/article/sony-sd-card-sales-suspended-memory-shortage"],
    ["The rise and fall of IBM's 4 Pi aerospace computers: an illustrated history", "https://www.righto.com/2026/03/ibm-4-pi-computer-history.html"],
    ["The bot situation on the internet is worse than you could imagine", "https://gladeart.com/blog/the-bot-situation-on-the-internet-is-actually-worse-than-you-could-imagine-heres-why"],
    ["Voyager 1 runs on 69 KB of memory", "https://news.ycombinator.com/item?id=voyager-memory"],
    ["Miasma: A tool to trap AI web scrapers in an endless poison pit", "https://github.com/austin-weeks/miasma"],
    ["Overestimation of microplastics potentially caused by scientists' gloves", "https://news.umich.edu/nitrile-and-latex-gloves-may-cause-overestimation-of-microplastics-u-m-study-reveals/"],
    ["Solar is winning the energy race", "https://www.dw.com/en/solar-is-winning-the-energy-race/a-76517556"],
    ["What if AI doesn't need more RAM but better math?", "https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more"],
    ["Show HN: Public transit systems as data – lines, stations, railcars", "https://publictransit.systems/"],
    ["LinkedIn uses 2.4 GB RAM across two tabs", "https://news.ycombinator.com/item?id=linkedin-ram"],
    ["Show HN: Sheet Ninja – Google Sheets as a CRUD Back End for Vibe Coders", "https://sheetninja.io/"],
    ["Typing and Keyboards (Grateful series)", "https://lzon.ca/posts/series/grateful/typing-and-keyboards/"],
    ["Lat.md: Agent Lattice: a knowledge graph for your codebase", "https://github.com/1st1/lat.md"],
    ["The road to electric – in charts and data [UK]", "https://www.rac.co.uk/drive/electric-cars/choosing/road-to-electric/"],
    ["When your AI tells you to do things you never asked it to do", "https://news.ycombinator.com/item?id=ai-instructions"],
    ["Rust in the Linux kernel: From 'experiment' to production code", "https://lwn.net/Articles/rust-linux-kernel-production/"],
    ["Why I prefer not to use an IDE (sometimes)", "https://news.ycombinator.com/item?id=no-ide"],
]

# ─── HELPERS ─────────────────────────────────────────────────────────────────
def esc(s):
    return html.escape(str(s))

def cat_slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def count_links(week):
    return sum(len(s["items"]) for s in week["sections"])

# ─── RENDER WEEK BLOCK ───────────────────────────────────────────────────────
def render_week(week_data, is_new=False):
    total = count_links(week_data)
    badge = '<span class="badge-new">LATEST</span>' if is_new else ''
    parts = [f'''
<div class="source-block">
  <div class="week-head">
    <h3><a href="{esc(week_data["url"])}" target="_blank">{esc(week_data["name"])}</a> {badge}</h3>
    <span class="meta">{esc(week_data["date"])} &middot; {total} curated links</span>
  </div>''']

    for sec in week_data["sections"]:
        h = sec["heading"]
        # Normalize heading to match SECTION_COLORS keys
        h_norm = h.replace("/", " / ").replace("  ", " ").strip()
        color = SECTION_COLORS.get(h_norm, SECTION_COLORS.get(h, "#475569"))
        slug = cat_slug(h_norm)
        id_attr = f' id="cat-{slug}"' if is_new else ''
        count = len(sec["items"])
        parts.append(f'''
  <div class="section-block"{id_attr}>
    <div class="sec-head">
      <span class="sec-badge" style="background:{color}22;color:{color};border:1px solid {color}44">{esc(h_norm)}</span>
      <span class="sec-count">{count} links</span>
    </div>
    <ul class="link-list">''')
        for title, url in sec["items"]:
            parts.append(f'      <li><a href="{esc(url)}" target="_blank" rel="noopener">{esc(title)}</a></li>')
        parts.append('    </ul>\n  </div>')

    parts.append('</div>')
    return '\n'.join(parts)

# ─── RENDER COMMUNITY CHANNELS ──────────────────────────────────────────────
def render_community():
    cards = []
    for ch in COMMUNITY_CHANNELS:
        cards.append(f'''    <a class="community-card" href="{esc(ch["url"])}" target="_blank" rel="noopener" style="border-left-color:{ch["color"]}">
      <div class="cname" style="color:{ch["color"]}">{esc(ch["name"])}</div>
      <div class="cmembers">{esc(ch["members"])} members</div>
      <div class="cdesc">{esc(ch["description"])}</div>
    </a>''')
    return '\n'.join(cards)

# ─── CATEGORY NAV ────────────────────────────────────────────────────────────
def render_nav():
    nav_parts = []
    for sec in W_LATEST["sections"]:
        h = sec["heading"]
        h_norm = h.replace("/", " / ").replace("  ", " ").strip()
        slug = cat_slug(h_norm)
        color = SECTION_COLORS.get(h_norm, SECTION_COLORS.get(h, "#475569"))
        label = h_norm.title().replace(" / ", "/")
        nav_parts.append(f'<a href="#cat-{slug}" style="color:{color};border-bottom:2px solid {color};padding-bottom:2px">{esc(label)}</a>')
    nav_parts.append('<a href="#feed" style="color:var(--mut)">Recent Feed</a>')
    nav_parts.append('<a href="#community" style="color:#f59e0b">Community</a>')
    return "\n      ".join(nav_parts)

# ─── BUILD FEED SECTION ──────────────────────────────────────────────────────
def render_feed():
    all_items = STARTME_ITEMS + BRUTALIST_ITEMS
    seen = set()
    rows = []
    for title, url in all_items:
        if url not in seen:
            seen.add(url)
            rows.append(f'      <li><a href="{esc(url)}" target="_blank" rel="noopener">{esc(title)}</a></li>')
    return '\n'.join(rows)

# ─── STATS BAR ───────────────────────────────────────────────────────────────
def render_stats():
    total_curated = count_links(W_LATEST) + count_links(W_PREV1) + count_links(W_PREV2)
    feed_count = len(STARTME_ITEMS) + len(BRUTALIST_ITEMS)
    total_all = total_curated + feed_count
    cats = len(W_LATEST["sections"])
    return f'''
    <div class="stats-bar">
      <div class="stat"><span class="stat-n">{total_all}</span><span class="stat-l">Total Links</span></div>
      <div class="stat"><span class="stat-n">{total_curated}</span><span class="stat-l">Curated Links</span></div>
      <div class="stat"><span class="stat-n">3</span><span class="stat-l">Weeks Covered</span></div>
      <div class="stat"><span class="stat-n">{cats}</span><span class="stat-l">Categories</span></div>
      <div class="stat"><span class="stat-n">{PULLED}</span><span class="stat-l">Pulled</span></div>
    </div>'''

# ─── FULL DIGEST ─────────────────────────────────────────────────────────────
def render_digest():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>🏰 DFIR Watchtower – {DATE_STR}</title>
<style>
:root{{
  --bg:#0f1117;--s1:#161b27;--s2:#1e2535;--acc:#60a5fa;--txt:#d1d5db;--mut:#6b7280;
  --brd:#2d3748;--grn:#10b981;--red:#ef4444;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:14px;line-height:1.6}}
a{{color:var(--acc);text-decoration:none}}
a:hover{{text-decoration:underline;opacity:.85}}
header{{background:linear-gradient(135deg,#0d1b2a 0%,#1a2744 50%,#0d1b2a 100%);border-bottom:1px solid var(--brd);padding:1.5rem 2rem;display:flex;align-items:center;gap:1rem}}
.logo{{font-size:2rem}}
.hdr-text h1{{font-size:1.4rem;font-weight:700;color:#fff;letter-spacing:.05em}}
.hdr-text p{{font-size:.8rem;color:var(--mut);margin-top:.2rem}}
.stats-bar{{display:flex;flex-wrap:wrap;gap:.5rem;padding:1rem 2rem;background:var(--s1);border-bottom:1px solid var(--brd)}}
.stat{{display:flex;flex-direction:column;align-items:center;background:var(--s2);border-radius:8px;padding:.5rem 1rem;min-width:110px}}
.stat-n{{font-size:1rem;font-weight:700;color:#fff}}
.stat-l{{font-size:.65rem;color:var(--mut);text-transform:uppercase;letter-spacing:.08em;margin-top:.1rem}}
nav{{position:sticky;top:0;z-index:100;background:var(--s1);border-bottom:1px solid var(--brd);padding:.6rem 2rem;display:flex;flex-wrap:wrap;gap:1rem;align-items:center}}
nav a{{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;text-decoration:none;transition:opacity .15s;white-space:nowrap}}
nav a:hover{{opacity:.7}}
.content{{max-width:1200px;margin:0 auto;padding:1.5rem 2rem}}
.source-block{{background:var(--s1);border:1px solid var(--brd);border-radius:12px;padding:1.25rem 1.5rem;margin-bottom:1.5rem}}
.week-head{{display:flex;align-items:baseline;gap:.75rem;margin-bottom:1rem;flex-wrap:wrap}}
.week-head h3{{font-size:1rem;font-weight:700;color:#fff}}
.week-head h3 a{{color:#fff}}
.badge-new{{background:#1d4ed8;color:#bfdbfe;font-size:.65rem;font-weight:700;padding:.2rem .5rem;border-radius:4px;letter-spacing:.08em;text-transform:uppercase}}
.meta{{font-size:.75rem;color:var(--mut)}}
.section-block{{margin-bottom:1.1rem;padding-bottom:1.1rem;border-bottom:1px solid var(--brd)}}
.section-block:last-child{{border-bottom:none;margin-bottom:0;padding-bottom:0}}
.sec-head{{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem}}
.sec-badge{{font-size:.68rem;font-weight:700;padding:.25rem .65rem;border-radius:20px;text-transform:uppercase;letter-spacing:.07em}}
.sec-count{{font-size:.7rem;color:var(--mut)}}
.link-list{{list-style:none;padding-left:.25rem;display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:.2rem .75rem}}
.link-list li{{padding:.15rem 0}}
.link-list li a{{font-size:.82rem;color:#93c5fd}}
.link-list li a:hover{{color:#dbeafe}}
.community-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:.9rem;margin-top:.75rem}}
.community-card{{background:var(--s2);border-radius:10px;padding:1rem 1.1rem;border-left:4px solid;transition:transform .15s,box-shadow .15s;text-decoration:none!important;display:block}}
.community-card:hover{{transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,0,0,.4)}}
.community-card .cname{{font-weight:700;font-size:.95rem;margin-bottom:.25rem;display:block}}
.community-card .cmembers{{font-size:.7rem;color:var(--mut);margin-bottom:.4rem}}
.community-card .cdesc{{font-size:.82rem;color:var(--txt);line-height:1.45}}
.feed-list{{list-style:none;padding:0;columns:2;column-gap:1.5rem}}
.feed-list li{{padding:.2rem 0;break-inside:avoid}}
.feed-list li a{{font-size:.82rem;color:#93c5fd}}
.feed-list li a:hover{{color:#dbeafe}}
footer{{text-align:center;padding:1.5rem;color:var(--mut);font-size:.75rem;border-top:1px solid var(--brd);margin-top:2rem}}
@media(max-width:768px){{
  .content{{padding:1rem}}
  nav{{padding:.5rem 1rem;gap:.6rem}}
  .feed-list{{columns:1}}
  .link-list{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>
<header>
  <div class="logo">🏰</div>
  <div class="hdr-text">
    <h1>DFIR WATCHTOWER</h1>
    <p>Weekly digest of Digital Forensics &amp; Incident Response intelligence — {DATE_STR}</p>
  </div>
</header>
{render_stats()}
<nav>
  {render_nav()}
</nav>
<div class="content">
  {render_week(W_LATEST, is_new=True)}
  {render_week(W_PREV1)}
  {render_week(W_PREV2)}

  <!-- RECENT FEED -->
  <div class="source-block" id="feed">
    <div class="week-head" style="margin-bottom:.75rem">
      <h3>Recent Feed</h3>
      <span class="meta">Latest from the DFIR community &amp; tech news</span>
    </div>
    <ul class="feed-list">
{render_feed()}
    </ul>
  </div>

  <!-- COMMUNITY CHANNELS -->
  <div class="source-block" id="community">
    <div class="week-head" style="margin-bottom:.75rem">
      <h3>Community Channels</h3>
      <span class="meta">DFIR &amp; security subreddits worth following</span>
    </div>
    <div class="community-grid">
{render_community()}
    </div>
  </div>
</div>
<footer>🏰 DFIR Watchtower &mdash; {PULLED} &mdash; <a href="https://github.com/forensicfellowship/DFIR_Watchtower" target="_blank">github.com/forensicfellowship/DFIR_Watchtower</a></footer>
</body>
</html>'''

# ─── WRITE OUTPUT ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    base = Path("/sessions/gallant-quirky-goodall/mnt/DFIR watchtower")
    base.mkdir(parents=True, exist_ok=True)

    content = render_digest()
    dated = base / f"watchtower_digest_{DATE_STR}.html"
    index = base / "index.html"

    dated.write_text(content, encoding="utf-8")
    index.write_text(content, encoding="utf-8")

    # Count total links for verification
    total_curated = count_links(W_LATEST) + count_links(W_PREV1) + count_links(W_PREV2)
    total_feed = len(STARTME_ITEMS) + len(BRUTALIST_ITEMS)
    print(f"✅ Written: {dated}")
    print(f"✅ Written: {index}")
    print(f"📊 Curated links: {total_curated}")
    print(f"📡 Feed items: {total_feed}")
    print(f"🔗 Total links: {total_curated + total_feed}")
