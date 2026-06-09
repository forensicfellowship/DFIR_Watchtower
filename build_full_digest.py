#!/usr/bin/env python3
"""DFIR Watchtower – Digest Builder"""
import html, re
from pathlib import Path
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc)
DATE_STR = NOW.strftime("%Y-%m-%d")
PULL_TIME = NOW.strftime("%Y-%m-%d %H:%M UTC")

# ── helpers ──────────────────────────────────────────────────────────────────
def esc(s): return html.escape(str(s))
def cat_slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

# ── section colour map ────────────────────────────────────────────────────────
SECTION_COLORS = {
    "FORENSIC ANALYSIS":            "#0e7490",
    "THREAT INTELLIGENCE / HUNTING":"#dc2626",
    "UPCOMING EVENTS":              "#7c3aed",
    "PRESENTATIONS / PODCASTS":     "#2563eb",
    "MALWARE":                      "#b45309",
    "MISCELLANEOUS":                "#047857",
    "SOFTWARE UPDATES":             "#1d4ed8",
}

# ── Latest digest data ────────────────────────────────────────────────────────────
W_LATEST = {
    "name": "June 7, 2026",
    "date": "June 7, 2026",
    "url":  "https://thisweekin4n6.com/2026/06/07/week-23-2026/",
    "sections": [
        {
            "heading": "FORENSIC ANALYSIS",
            "items": [
                ("How To Investigate Video Evidence: Workflows, Pitfalls and Best Practices",
                 "https://blog.ampedsoftware.com/2026/06/03/investigate-video-evidence"),
                ("That still only counts as one! – iLEAPP Sticker Animation",
                 "https://cp-df.com/en/blog/zalo.html"),
                ("DFIR+AI Primer: When Not To Use GenAI",
                 "https://www.cybertriage.com/ai/dfirai-primer-when-not-to-use-genai/"),
                ("Forensic Implications of Apple Stolen Device Protection",
                 "https://blog.elcomsoft.com/2026/06/forensic-implications-of-apple-stolen-device-protection/"),
                ("Memory Suspicious Processes",
                 "https://forensafe.com/blogs/memory-suspicious.html"),
                ("Memory Services",
                 "https://forensafe.com/blogs/memory-services.html"),
                ("Revisiting the APFS Series",
                 "https://jtsylve.blog/post/2026/06/01/Revisiting-the-APFS-Series"),
                ("Space Manager",
                 "https://jtsylve.blog/post/2026/06/02/APFS-Space-Manager"),
                ("The Reaper",
                 "https://jtsylve.blog/post/2026/06/03/APFS-Reaper"),
                ("EFI Jumpstart",
                 "https://jtsylve.blog/post/2026/06/04/APFS-EFI-Jumpstart"),
                ("Hard Links and Siblings",
                 "https://jtsylve.blog/post/2026/06/05/APFS-Siblings"),
                ("Canonical Multipass Forensics 101",
                 "https://matthewplascencia.substack.com/p/canonical-multipass-forensics-101"),
            ],
        },
        {
            "heading": "THREAT INTELLIGENCE / HUNTING",
            "items": [
                ("Red Hat npm Packages Compromised to Spread a Credential-Stealing Worm",
                 "https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm"),
                ("Why EDR and proxy won’t save you from supply chain malware",
                 "https://www.aikido.dev/blog/edr-proxy-wont-protect-supply-chain-malware"),
                ("Popping Root on UniFi OS Server: Unauthenticated RCE Chain Detection & Analysis",
                 "https://bishopfox.com/blog/popping-root-on-unifi-os-server-unauthenticated-rce-chain-detection-analysis"),
                ("Auditing GitLab: The CI/CD Kill Chain",
                 "https://www.blackhillsinfosec.com/auditing-gitlab-the-ci-cd-kill-chain/"),
                ("The State of Ransomware: May 2026",
                 "https://www.blackfog.com/the-state-of-ransomware-may-2026/"),
                ("Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts",
                 "https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/"),
                ("Intelligence Insights: May 2026",
                 "https://www.bridewell.com/insights/blogs/detail/intelligence-insights-may-2026"),
                ("UK Cybercrime Journal: British Universities Struck by ShinyHunters Before Exam Season",
                 "https://blog.bushidotoken.net/2026/05/uk-cybercrime-journal-british.html"),
                ("How a Dangling DNS Entry Can Lead to a Subdomain Takeover",
                 "https://censys.com/blog/dangling-dns-subdomain-takeover/"),
                ("Sintesi riepilogativa delle campagne malevole nella settimana del 30 maggio – 5 giugno",
                 "https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-30-maggio-5-giugno/"),
                ("The Server Seizure That Affects Also Iran’s Cyber Operations",
                 "https://blog.checkpoint.com/security/the-server-seizure-that-affects-also-irans-cyber-operations/"),
                ("1st June – Threat Intelligence Report",
                 "https://research.checkpoint.com/2026/1st-june-threat-intelligence-report/"),
                ("Impersonation, Click Hijacking, and TDS: Inside a Malware Distribution Ecosystem",
                 "https://research.checkpoint.com/2026/impersonation-click-hijacking-and-tds-inside-a-malware-distribution-ecosystem/"),
                ("Fraud, Ransomware, and Fake Apps Are Already Targeting FIFA 2026",
                 "https://blog.checkpoint.com/exposure-management/fraud-ransomware-and-fake-apps-are-already-targeting-fifa-2026/"),
                ("Hypotheses, telemetry, and human judgment: Inside Cisco Talos Threat Hunting",
                 "https://blog.talosintelligence.com/hypotheses-telemetry-and-human-judgment-inside-cisco-talos-threat-hunting/"),
                ("How an Unauthenticated MCP Server Led to SSRF, LFI, and AWS Credential Theft",
                 "https://www.cloudsek.com/blog/aivigil-mcp-security-case-study"),
                ("Embedded Threats: How Attackers Weaponize Legitimate Emails",
                 "https://cofense.com/blog/embedded-threats-how-attackers-weaponize-legitimate-emails"),
                ("我们绕过了 GarudaDefender 整套 Frida 检测，但这已经不是重点了",
                 "https://www.ctfiot.com/309612.html"),
                ("APT-C-26（Lazarus）组织利用CVE-2025-55182与Copperhedge组件的攻击行动分析",
                 "https://www.ctfiot.com/309562.html"),
                ("C-Suite Impersonation in the Gulf: How Threat Actors Are Targeting UAE & Saudi Executives in 2026",
                 "https://cyble.com/blog/ceo-fraud-executive-impersonation-gulf-firms/"),
                ("Weekly Intelligence Report – 05 Jun 2026",
                 "https://www.cyfirma.com/news/weekly-intelligence-report-05-jun-2026/"),
                ("The Interesting Case of WSL for Payload Staging",
                 "https://detect.fyi/the-interesting-case-of-wsl-for-payload-staging-bfaa0f69329a?source=rss-5036c3f97701------2"),
                ("Inside Modern Supply Chain Intrusions: From CI/CD Abuse to Ecosystem-Wide Compromise",
                 "https://darkatlas.io/blog/inside-modern-supply-chain-intrusions-from-ci-cd-abuse-to-ecosystem-wide-compromise"),
                ("Deep KQL Analysis with Kustology",
                 "https://detect.fyi/deep-kql-analysis-with-kustology-f07de9b02829?source=rss----d5fd8f494f6a---4"),
                ("The Interesting Case of WSL for Payload Staging",
                 "https://detect.fyi/the-interesting-case-of-wsl-for-payload-staging-bfaa0f69329a?source=rss----d5fd8f494f6a---4"),
                ("Weekly Threat Infrastructure Investigation(Week23)",
                 "https://disconinja.hatenablog.com/entry/2026/06/07/111734"),
                ("Dragos Industrial Ransomware Analysis for the First Quarter of 2026",
                 "https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026"),
                ("Device Code Phishing Forensics: What We Learned Investigating BEC in the Wild",
                 "https://research.eye.security/device-code-phishing-forensics/"),
                ("FIFA World Cup 2026: Mapping the Global Cyber Scam Ecosystem Targeting Fans",
                 "https://falconfeeds.io/blogs/fifa-world-cup-2026-global-cyber-scam-ecosystem-analysis/"),
                ("FalkonC2 is Getting Ridiculously Stealthy",
                 "https://flare.io/learn/resources/blog/falkonc2"),
                ("KeyCat Stealer Uncovered: Inside a $40 Multi-Platform Infostealer with Telegram C2 and Active Staging Infrastructure",
                 "https://flare.io/learn/resources/blog/keycat-stealer-multi-platform-infostealer"),
                ("Understanding Illicit Ecosystems: XSS and the Current State of the Russian-Speaking Underground",
                 "https://flashpoint.io/blog/understanding-illicit-ecosystems-xss-russian-speaking-underground/"),
                ("Cybercriminals Are Targeting the FIFA World Cup 2026",
                 "https://www.fortinet.com/blog/threat-research/cybercriminals-are-targeting-the-fifa-world-cup-2026"),
                ("Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms",
                 "https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms/"),
                ("Cryptocurrency Scams: The 10 Most Common Types and How They Work",
                 "https://www.group-ib.com/blog/cryptocurrency-scams/"),
                ("Error 524 Decoy: Unmasking a Global Smishing Operation Hiding Behind Error Pages",
                 "https://www.group-ib.com/blog/error-524-decoy-smishing/"),
                ("The Anatomy of a Destructive Attack",
                 "https://threatresearch.ext.hp.com/the-anatomy-of-a-destructive-attack/"),
                ("PCPJack Hijacked 230 AWS, GCP, and Azure Servers to Run a Hidden SMTP Relay Network",
                 "https://hunt.io/blog/pcpjack-230-cloud-servers-smtp-proxy-network-sliver-chisel"),
                ("Gentlemen Ransomware",
                 "https://www.intel471.com/blog/gentlemen-ransomware"),
                ("Threat Hunting Case Study: FileFix",
                 "https://www.intel471.com/blog/threat-hunting-case-study-filefix"),
                ("How attackers are gaining access to LLM inference",
                 "https://intezer.com/blog/how-attackers-access-llm-inference/"),
                ("Analyste CTI et LLM: exemple d’une collaboration fructueuse",
                 "https://www.intrinsec.com/analyste-cti-et-llm/"),
                ("How to respond to an incident in Kubernetes | AKS | Invictus Incident Response",
                 "https://invictus-ir.com/news/incident-response-in-kubernetes-aks"),
                ("Living Off The Land – Built-In Pwning",
                 "https://www.lares.com/blog/living-off-the-land/"),
                ("Outlook 365 for the PWN",
                 "https://www.lares.com/blog/outlook365/"),
                ("The Demon Arrives Later: A Havoc Stager Hides Behind Microsoft Defender DLP",
                 "https://www.levelblue.com/blogs/spiderlabs-blog/the-demon-arrives-later-a-havoc-stager-hides-behind-microsoft-defender-dlp"),
                ("macOS ClickFix Social Engineering Campaigns",
                 "https://www.levelblue.com/blogs/spiderlabs-blog/macos-clickfix-social-engineering-campaigns"),
                ("ClickFix Is Now Hiring: From Job Platform Impersonation to Python-Based RAT Delivery",
                 "https://www.levelblue.com/blogs/spiderlabs-blog/clickfix-is-now-hiring-from-job-platform-impersonation-to-python-based-rat-delivery"),
                ("Game Over: WeedHack – The Rise of Minecraft Malware-as-a-Service Campaigns",
                 "https://www.mcafee.com/blogs/other-blogs/mcafee-labs/weedhack-minecraft-malware-as-a-service-campaign-research/"),
                ("Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign",
                 "https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/"),
                ("Securing CI/CD in an agentic world: Claude Code Github action case",
                 "https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/"),
                ("New Mac stealer SHub Reaper is spoofing Apple, Google, and Microsoft",
                 "https://moonlock.com/mac-stealer-shub-reaper"),
                ("Fake ChatGPT site unleashes the dangerous Odyssey Stealer",
                 "https://moonlock.com/fake-chatgpt-sites-odyssey-stealer"),
                ("How China’s Cyber Operations – and the Contractors Behind Them – Target Critics Abroad",
                 "https://www.nattothoughts.com/p/how-chinas-cyber-operations-and-the-610"),
                ("Detecting Nimbus Manticore and their sideloading infection chains",
                 "https://www.nextron-systems.com/2026/06/01/detecting-nimbus-manticore-and-their-sideloading-infection-chains/"),
                ("The Detection & Response Chronicles: Covert Operations Through QEMU",
                 "https://blog.nviso.eu/2026/06/04/the-detection-response-chronicles-covert-operations-through-qemu/"),
                ("The Software Supply Chain Malware Landscape: January – May 2026",
                 "https://opensourcemalware.com/blog/software-supply-chain-malware-landscape"),
                ("The Blight Reaches Microsoft: 73 Repos Disabled in 105 Seconds",
                 "https://opensourcemalware.com/blog/miasma-reaches-azure"),
                ("The Evolution of Malware",
                 "https://osintteam.blog/the-evolution-of-malware-fa60c1984c02?source=rss----2983bc435765---4"),
                ("The Gentlemen Ransomware: Threat Profile",
                 "https://osintteam.blog/the-gentlemen-ransomware-threat-profile-b416da89a80d?source=rss----2983bc435765---4"),
                ("New npm Supply Chain Attack: @redhat-cloud-services Compromised",
                 "https://www.ox.security/blog/new-npm-supply-chain-attack-redhat-cloud-services-compromised/"),
                ("Six Stages Deep and an Endless Loop: Shai-Hulud Is Getting Sophisticated",
                 "https://www.ox.security/blog/six-stages-deep-and-an-endless-loop-shai-hulud-is-getting-sophisticated/"),
                ("IronWorm Supply Chain Malware Hits npm",
                 "https://www.ox.security/blog/ironworm-supply-chain-malware-hits-npm/"),
                ("600,000 Monthly Downloads Affected: Miasma Supply Chain Attack Is Back on npm",
                 "https://www.ox.security/600000-monthly-downloads-affected-miasma-supply-chain-attack-is-back-on-npm/"),
                ("Malware-Slop 2: Malicious npm Package Leaks Its Own Bot’s Telegram Private Token",
                 "https://www.ox.security/blog/malware-slop-2-malicious-npm-package-leaks-its-own-bots-telegram-private-token/"),
                ("Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor",
                 "https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/"),
                ("We Added a Detection Rule. We Were Not Expecting This.",
                 "https://profero.io/blog/hiddenperms/"),
                ("TA4922: The Suspected Chinese Crime Group is Going Global",
                 "https://www.proofpoint.com/us/blog/threat-insight/ta4922-suspected-chinese-crime-group-going-global"),
                ("Using the Pyramid of Pain for threat detection in the AI era",
                 "https://pushsecurity.com/blog/the-pyramid-of-pain-in-the-ai-era"),
                ("Iran Expands Handala Brand to Physical Threats",
                 "https://www.recordedfuture.com/research/iran-handala-physical-threats"),
                ("Investigating suspicious AI workflows in Microsoft Entra Agent ID: Agent’s user account",
                 "https://redcanary.com/blog/threat-detection/entra-id-ai-workflows-teams/"),
                ("ReliaQuest’s Agentic AI Uncovers New China-Linked Cluster OP-512",
                 "https://reliaquest.com/blog/threat-spotlight-reliaquests-agentic-ai-uncovers-new-china-linked-cluster-op-512/"),
                ("YARA-X 1.17.0 Release, (Sun, May 31st)",
                 "https://isc.sans.edu/diary/rss/33032"),
                ("Unidentified RAT pushes NetSupport RAT, (Mon, Jun 1st)",
                 "https://isc.sans.edu/diary/rss/33034"),
                ("New Wave Of Phishing Emails with SVG Files, (Tue, Jun 2nd)",
                 "https://isc.sans.edu/diary/rss/33040"),
                ("Continuing Scans for swagger.json, (Wed, Jun 3rd)",
                 "https://isc.sans.edu/diary/rss/33044"),
                ("Microsoft’s Coreutils for Windows, (Thu, Jun 4th)",
                 "https://isc.sans.edu/diary/rss/33048"),
                ("The Evil MSI Background is Back!, (Fri, Jun 5th)",
                 "https://isc.sans.edu/diary/rss/33054"),
                ("GorgonAgora: 4,800+ fake storefronts skim cards across hundreds of impersonated brands",
                 "https://sansec.io/research/gorgonagora-fake-storefront-skimming-network"),
                ("Magecart skimmer turns Stripe into a malware command server",
                 "https://sansec.io/research/stripe-api-skimmer-infrastructure"),
                ("Containers on fire: from container escapes to supply chain attacks",
                 "https://securelist.com/container-attack-vectors/120010/"),
                ("Wardriving assessment across Mexico: Preparing for the 2026 World Cup",
                 "https://securelist.com/wardriving-assessment-in-mexico-fifa-world-cup-2026/119996/"),
                ("Argamal: Malware hidden in hentai games",
                 "https://securelist.com/argamal-rat-distributed-with-hentai-games/119999/"),
                ("FSB’s matryoshka #1/3 – Gamaredon’s gifts that keeps unpacking – GammaPhish and GammaWorm",
                 "https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/"),
                ("FSB’s matryoshka #2/3 – Gamaredon’s gifts that keeps unpacking – GammaLoad",
                 "https://blog.sekoia.io/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload/"),
                ("FSB’s matryoshka #3/3 – Gamaredon’s gifts that keeps unpacking – GammaSteel",
                 "https://blog.sekoia.io/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel/"),
                ("Best Incident Response Techniques for Ransomware Attacks to Minimize Damage",
                 "https://www.seqrite.com/blog/best-incident-response-techniques-for-ransomware-attacks-to-minimize-damage/"),
                ("Dark Web Profile: BlindEagle",
                 "https://socradar.io/blog/dark-web-profile-blindeagle/"),
                ("Dark Web Profile: Vect Ransomware",
                 "https://socradar.io/blog/dark-web-profile-vect-ransomware/"),
                ("Multiple redhat-cloud-services npm Packages compromised",
                 "https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised"),
                ("Miasma npm Supply Chain Attack: Self-Spreading Worm via Phantom Gyp",
                 "https://www.stepsecurity.io/blog/binding-gyp-npm-supply-chain-attack-spreads-like-worm"),
                ("Armenia: Bashe Claims to Have Purchased a Database of More Than 30,000 Voters from a Pro-Turkish Group",
                 "https://www.suspectfile.com/armenia-bashe-claims-to-have-purchased-a-database-of-more-than-30000-voters-from-a-pro-turkish-group/"),
                ("Singing River Health System: Between Ransomware, Legal Disputes, and Recurring Vulnerabilities",
                 "https://www.suspectfile.com/singing-river-health-system-between-ransomware-legal-disputes-and-recurring-vulnerabilities/"),
                ("Espionage Campaign Targeted Stock Exchange Executive for Five Months",
                 "https://www.security.com/threat-intelligence/stock-exchange-espionage"),
                ("Security briefing: May 2026",
                 "https://webflow.sysdig.com/blog/security-briefing-may-2026"),
                ("Agentic threat actor hits the orchestration plane: AI agent-driven container escape",
                 "https://webflow.sysdig.com/blog/agentic-threat-actor-hits-the-orchestration-plane-ai-agent-driven-container-escape"),
                ("Own Goal? Piracy as an Attack Vector to Target Football Fans",
                 "https://www.threatfabric.com/blogs/own-goal-piracy-as-an-attack-vector-to-target-football-fans"),
                ("Oil & Gas Sector Cyber Threat Intelligence Report 2026",
                 "https://threatmon.io/oil-gas-sector-cyber-threat-intelligence-report-2026/"),
                ("The Privileged Roles Nobody Talks About",
                 "https://trustedsec.com/blog/the-privileged-roles-nobody-talks-about"),
                ("From Conti to The Gentlemen: tooling evolved, gaps didn’t. by Lucie Cardiet",
                 "https://www.vectra.ai/blog/from-conti-to-the-gentlemen-tooling-evolved-gaps-didnt"),
                ("YARA Rules: A Complete Guide with Best Practices and Use Cases",
                 "https://www.vmray.com/yara-rules-guide/"),
                ("VerdantBamboo: Just Another BRICKSTORM in the Firewall",
                 "https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/"),
                ("Miasma: Supply Chain Attack Targeting RedHat npm Packages",
                 "https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages"),
                ("Attackers Actively Exploiting Critical Vulnerability in Everest Forms Pro Plugin",
                 "https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/"),
            ],
        },
        {
            "heading": "UPCOMING EVENTS",
            "items": [
                ("ADF Weekly Mobile Training Sessions",
                 "https://register.gotowebinar.com/rt/5995208548160709981"),
                ("ADF Weekly Computer Training Sessions",
                 "https://register.gotowebinar.com/rt/8364955173180524123"),
                ("ClickOnce Commander: Weaponizing Trusted Microsoft Deployment w/ Steve",
                 "https://www.youtube.com/watch?v=acijx_Tb5DU"),
                ("BHIS – Talkin’ Bout [infosec] News 2026-06-08",
                 "https://www.youtube.com/watch?v=_o5hjjtflc4"),
                ("From Seizure to Intelligence: Practical Digital Evidence Workflows for Drug Investigations",
                 "https://cellebrite.com/en/resources/webinars/from-seizure-to-intelligence-practical-digital-evidence-workflows-for-drug-investigations/"),
                ("Legal Unpacked S1:E9 // Digital evidence in criminal prosecutions: Discovery obligations, requests, and practical strategy",
                 "https://www.magnetforensics.com/resources/legal-unpacked-s1e9-digital-evidence-in-criminal-prosecutions-discovery-obligations-requests-and-practical-strategy/?utm_source=ThisWeekin4n6&utm_medium=Organic&utm_campaign=2026_Review_Social"),
                ("Ask Me Anything: Strengthening eDiscovery with digital forensics",
                 "https://www.magnetforensics.com/resources/ask-me-anything-strengthening-ediscovery-with-digital-forensics/?utm_source=ThisWeekin4n6&utm_medium=Organic&utm_campaign=2026_AxiomCyber_Social"),
                ("Drowning in data…Practical cloud storage and data migration strategies",
                 "https://www.magnetforensics.com/resources/drowning-in-datapractical-cloud-storage-and-data-migration-strategies/?utm_source=ThisWeekin4n6&utm_medium=Organic&utm_campaign=2026_MagnetOne_Social"),
                ("Poisoned Packages & Stolen Secrets: The Rise of Supply Chain Attacks",
                 "https://www.youtube.com/watch?v=PeJc0e_Rzrw"),
                ("The Anatomy of Cyber Attacks Affecting OT Organizations",
                 "https://www.sygnia.co/webinars/the-anatomy-of-cyber-attacks-affecting-ot-organizations/"),
            ],
        },
        {
            "heading": "PRESENTATIONS / PODCASTS",
            "items": [
                ("The AI Investigative Framework Interview with Heather Barnhart",
                 "https://www.youtube.com/watch?v=bTHIw1ob4i4"),
                ("AI in Digital Forensics panel hosted by MSAB at Techno Security East 2026",
                 "https://www.youtube.com/watch?v=5kaVPCXROdw"),
                ("EP26 When AI Features Create Zero-Click Exploits: The Pixel 9 Chain with Seth Jenkins",
                 "https://www.buzzsprout.com/2414128/episodes/19250444-ep26-when-ai-features-create-zero-click-exploits-the-pixel-9-chain-with-seth-jenkins.mp3"),
                ("Domain Search is the CSI Linux Case Management System",
                 "https://www.youtube.com/watch?v=l1QGzEFLZao"),
                ("Email Search OSINT within the CSI Linux Case Management System",
                 "https://www.youtube.com/watch?v=IdYNkfsbPmo"),
                ("Techno Live",
                 "https://www.youtube.com/watch?v=Mj6v0F7p95E"),
                ("Techno Day 2 – S2 Data",
                 "https://www.youtube.com/watch?v=F2p1mhbx59c"),
                ("Live from Techno Security in Myrtle Beach with JJ from ADF Solutions",
                 "https://www.youtube.com/watch?v=gKANahrNRmw"),
                ("Live at Techno Security with Alex from Lumyx!",
                 "https://www.youtube.com/watch?v=8fSQfTpmnTg"),
                ("Techno Day 3",
                 "https://www.youtube.com/watch?v=p1YcinZejts"),
                ("Techno Day 2 – Martino from Amped",
                 "https://www.youtube.com/watch?v=J-Yziap3htQ"),
                ("Techno Day 2 – BlackRainbow",
                 "https://www.youtube.com/watch?v=_Su8GXRX8JM"),
                ("Techno Day 2 – Matt Danner from Monolith Forensics",
                 "https://www.youtube.com/watch?v=YoQ0DH7a-n0"),
                ("Jennifer from Techno Security Conference – Techno Day 3",
                 "https://www.youtube.com/watch?v=R6q17knqomI"),
                ("DATAPILOT – Techno Day 3",
                 "https://www.youtube.com/watch?v=sna1RBMRyBg"),
                ("Jessica Hyde – Techno Day 3",
                 "https://www.youtube.com/watch?v=O3Di_u_2Kgk"),
                ("[Workshop] Saying Goodbye to the #US Stream – Analyzing String Obfuscation",
                 "https://www.youtube.com/watch?v=B6lBZC6XEJo"),
                ("CVE | FIRST VulnCon 2026 & Annual CNA Summit",
                 "https://www.youtube.com/watch?v=bBunxDmWb0A&list=PLBAUUhONOrO_yESOH6JnwWBoRdDRVXDr0"),
                ("Episode 58: Cheng-Lin Yang and Lily Chen, CyCraft, FIRSTCON26 Speakers",
                 "https://www.youtube.com/watch?v=32FPCLBdV1k"),
                ("_declassified Ep. 2 | Unfriendly Followers: The Black Market For Your Identity",
                 "https://www.youtube.com/watch?v=T8_KtQwxtcE"),
                ("Session Hijacking Explained in 3 Min",
                 "https://www.youtube.com/watch?v=mDBWx99Av34"),
                ("IR – SOC340 – Apache Tomcat Serialized Payload RCE (CVE-2025-24813)",
                 "https://www.youtube.com/watch?v=LcwI68q8_bY"),
                ("A Linux Backdoor is For Sale on the Dark Web",
                 "https://www.youtube.com/watch?v=3YB4XGy8xwE"),
                ("JHT Course Launch! Windows Maldev 6",
                 "https://www.youtube.com/watch?v=a8stY1VjhXw"),
                ("BIG SHOW TODAY & AI vibes",
                 "https://www.youtube.com/watch?v=hG1imCvG7B8"),
                ("CTI for SMB: How Small Businesses Can Operationalize Threat Intelligence for Free",
                 "https://kravensecurity.com/cti-for-smb/"),
                ("Cyber Unpacked S3:E3 // The burnout equation: Sustaining your SOC and IR teams for the long game",
                 "https://www.magnetforensics.com/resources/cyber-unpacked-s3e3-the-burnout-equation-sustaining-your-soc-and-ir-teams-for-the-long-game/?utm_source=ThisWeekin4n6&utm_medium=Organic&utm_campaign=2026_AxiomCyber_Social"),
                ("Supply Chain Attacks: Open Source or Open Door?",
                 "https://traffic.megaphone.fm/CYBW3604416092.mp3"),
                ("Custom Report Templates – Monolith Mondays",
                 "https://www.youtube.com/watch?v=TMzwg9OGFBI"),
                ("Metrics Reports in Monolith",
                 "https://www.youtube.com/watch?v=W45UWV7QL9o"),
                ("#MSABMonday – XPAA Course",
                 "https://www.youtube.com/watch?v=ed7rEN6S1Zk"),
                ("MYDFIR DFIR Course: Overview (NEW DFIR COURSE)",
                 "https://www.youtube.com/watch?v=UBSkEZoBvEg"),
                ("TryHackMe AI Security 1 (AI1) Certification | Is It Good? (GIVEAWAY)",
                 "https://www.youtube.com/watch?v=mNSooKtIwEs"),
                ("Failure is Not an Option! A Reliable Process to Exploit STM32F2/F4 Microcontrollers, with Joe Grand",
                 "https://www.youtube.com/watch?v=5Z3rUOm9MLc"),
                ("OpenSourceMalware Show Episode #7 – June 3, 2026",
                 "https://opensourcemalware.com/blog/opensourcemalware-show-episode07"),
                ("S2 E3: The 12 Invoices",
                 "https://www.youtube.com/watch?v=clPbMf97aHc"),
                ("A Day in the Life of an MDR Analyst: Inside the Modern SOC",
                 "https://www.rapid7.com/blog/post/it-day-in-the-life-mdr-analyst-inside-the-modern-soc"),
                ("She Convinced the Pentagon to Let Hackers In. Legally. With Katie Moussouris",
                 "https://www.youtube.com/watch?v=o9b5fbXLP00"),
                ("SANS Cloud Security: Securing Gen AI RAG Data using Azure AI Search with Eric Johnson",
                 "https://www.youtube.com/watch?v=UgWSOr2SZhc"),
                ("Disinformation in 2026: How Influence Operations Work and How to Spot Them",
                 "https://www.youtube.com/watch?v=giG5VjFpvO8"),
                ("Detection Coverage: Measuring What You Can Actually Detect",
                 "https://www.youtube.com/watch?v=el17__sCRRE"),
                ("LABScon25 Replay | Gamaredon x Turla: Unveiling a 2025 Espionage Alliance Targeting Ukraine",
                 "https://www.sentinelone.com/labs/labscon25-replay-gamaredon-x-turla-unveiling-a-2025-espionage-alliance-targeting-ukraine/"),
                ("The Log Collector | RECON ITR Overview",
                 "https://www.youtube.com/watch?v=cnbdxCm15bo"),
                ("How Akira hits thousands of SMBs with $50K-$150K ransoms undetected | Alex Bovicelli",
                 "https://www.youtube.com/watch?v=KU2kUtKzQEw"),
                ("Fast16, Fanny, and Stuxnet: Cyber Paleontology Redux",
                 "https://securityconversations.fireside.fm/fast16-fanny-and-stuxnet-cyber-paleontology-redux"),
            ],
        },
        {
            "heading": "MALWARE",
            "items": [
                ("From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises",
                 "https://any.run/cybersecurity-blog/monoglyphrat-attacks-us-enterprise/"),
                ("Q1 2026 Cyber Risk Report: Insights from 2.1 Million Malware and Phishing Investigations",
                 "https://any.run/cybersecurity-blog/cyber-risk-report-q1-2026/"),
                ("Crypto Guest at Dawn Endpoint (Midnight) ransomware analysis",
                 "https://asec.ahnlab.com/en/93932/"),
                ("Android.MagicAd trojan displays ads despite all restrictions",
                 "https://news.drweb.com/show/?i=15262&lng=en&c=5"),
                ("PHANTOMPULSE: anatomy of a hijackable blockchain-C2 RAT",
                 "https://www.elastic.co/security-labs/blockchain-c2-phantompulse-rat-sinkhole"),
                ("Tracking APT28 PixyNetLoader: Evolutions from 2024 to 2026",
                 "https://blog.exatrack.com/Tracking_APT28_PixyNetLoader/"),
                ("Inside the Cross-Platform Propagation of a New Gafgyt Variant C0XMO",
                 "https://www.fortinet.com/blog/threat-research/inside-cross-platform-propagation-of-new-gafgyt-variant-c0xmo"),
                ("Browser Spy-Ons: Threat Actor’s Extension Hijack Your AI Conversations",
                 "https://blog.gdatasoftware.com/2026/06/38428-browser-addons-spy-on-ai-chats"),
                ("Inside an Active STX RAT Supply Chain Campaign",
                 "https://www.cyderes.com/howler-cell/cpuid-hwmonitor-xvpn-dll-sideloading-stx-rat"),
                ("VECT: Ransomware That Can’t Decrypt",
                 "https://www.morphisec.com/blog/vect-ransomware-that-cant-decrypt/"),
                ("Unmasking Quellostanco: How a Git Commit Exposed a Threat Actor Targeting Egyptian Infrastructure (co-authored)",
                 "https://m4lcode.github.io/unmasking-quellostanco-how-a-git-commit-exposed-a-threat-actor-targeting-egyptian-infrastructure"),
                ("31 Red Hat npm packages backdoored in 72 seconds",
                 "https://www.reversinglabs.com/blog/31-red-hat-cloud-service-npm-packages-backdoored-in-72-seconds"),
                ("How 56 npm packages used binding.gyp to steal CI/CD secrets",
                 "https://www.reversinglabs.com/blog/npm-bindinggyp-cicd-secrets"),
                ("Diamotrix",
                 "https://rexorvc0.com/2026/06/03/Diamotrix/"),
                ("Analysis of DirtyFrag (Vulnerability)",
                 "https://medium.com/@shubhandrew/analysis-of-dirtyfrag-vulnerability-7ea2b9448a03?source=rss-f4e5a887e2cb------2"),
                ("Miasma supply chain attack: malicious code found in @redhat-cloud-services npm packages",
                 "https://snyk.io/blog/miasma-supply-chain-attack-malicious-code-redhat-cloud-services-npm-packages/"),
                ("Protestware by open source maintainer to hinder agentic coding: The jqwik 1.10.0 Prompt Injection",
                 "https://snyk.io/blog/protestware-open-source-maintainer-qwik-1-10-0-prompt-injection/"),
                ("Node-gyp Supply Chain Compromise: A Self-Propagating npm Worm That Hides in binding.gyp",
                 "https://snyk.io/blog/node-gyp-supply-chain-compromise-self-propagating-npm-worm-binding-gyp/"),
                ("Famous Chollima Targets PHP Developers Through Compromised Packagist Package",
                 "https://socket.dev/blog/famous-chollima-targets-php-developers-through-compromised-packagist-package?utm_medium=feed"),
                ("Mini Shai-Hulud Campaign Hits Red Hat Cloud Services npm Packages",
                 "https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages?utm_medium=feed"),
                ("Pointing a Cursor at evading detection",
                 "https://www.sophos.com/en-us/blog/pointing-a-cursor-at-evading-detection"),
                ("You do surprise me.exe: An unexpected executable in Hola Browser",
                 "https://www.sophos.com/en-us/blog/you-do-surprise-me-exe-an-unexpected-executable-in-hola-browser"),
            ],
        },
        {
            "heading": "MISCELLANEOUS",
            "items": [
                ("little secret of msconfig.exe",
                 "https://www.hexacorn.com/blog/2026/06/07/little-secret-of-msconfig-exe/"),
                ("LEAPPs.org – Latest changes!",
                 "https://abrignoni.blogspot.com/2026/05/leappsorg-latest-changes.html"),
                ("When digital evidence follows you home in DFIR teams",
                 "https://andreafortuna.org/2026/06/05/dfir-analyst-psychological-impact/"),
                ("Being Cross-Examined by AI",
                 "https://www.linkedin.com/pulse/being-cross-examined-ai-andrew-garrett-z4dfc/"),
                ("The difference between “No one will hire me” and “I am no longer professionally allowed to do this DFIR work”",
                 "https://brettshavers.com/brett-s-blog/entry/the-difference-between-no-one-will-hire-me-and-i-can-no-longer-professionally-allowed-to-do-this-dfir-work"),
                ("AI in Digital Forensics: 10 Best Practices for Investigators",
                 "https://cellebrite.com/en/blog/ai-in-digital-forensics-best-practices/"),
                ("Microsoft Defender for Office 365 Part 10: Attack Simulation Training",
                 "https://cyberboo.substack.com/p/microsoft-defender-office-365-attack-simulation-training"),
                ("Securus Jail Call Monitoring, Cities Lose Control Over Surveillance, Police IDs Made from Video, Nina Loshkajian Answers 5 Questions & More",
                 "https://digitalforensicslas.substack.com/p/securus-jail-surveillance-cities"),
                ("DFIR Jobs Update – 06/01/26",
                 "https://dfirdominican.com/dfir-jobs-update-06-01-26/"),
                ("Belkasoft Releases Belkasoft X v2.11, Expanding AI-Powered Investigations And Evidence Extraction Capabilities",
                 "https://www.forensicfocus.com/news/belkasoft-releases-belkasoft-x-v2-11-expanding-ai-powered-investigations-and-evidence-extraction-capabilities/"),
                ("Burnout, PTSD, Suicidal Thoughts – The DFIR Well-Being Study Results Are In",
                 "https://www.forensicfocus.com/podcast/burnout-ptsd-suicidal-thoughts-the-dfir-well-being-study-results-are-in/"),
                ("Digital Forensics Jobs Round-Up, June 01 2026",
                 "https://www.forensicfocus.com/jobs/digital-forensics-jobs-round-up-june-01-2026/"),
                ("Andreas Antonsen, Founder, STNDRDS AB",
                 "https://www.forensicfocus.com/interviews/andreas-antonsen-founder-stndrds-ab/"),
                ("Video Timing In Amped FIVE",
                 "https://www.forensicfocus.com/articles/video-timing-in-amped-five/"),
                ("Digital Forensics Round-Up, June 03 2026",
                 "https://www.forensicfocus.com/news/digital-forensics-round-up-june-03-2026/"),
                ("Forensic Focus Digest, June 05 2026",
                 "https://www.forensicfocus.com/news/forensic-focus-digest-june-05-2026/"),
                ("How Freeland Is Using Detego Technology to Dismantle Wildlife Trafficking Networks",
                 "https://www.forensicfocus.com/news/how-freeland-is-using-detego-technology-to-dismantle-wildlife-trafficking-networks/"),
                ("Welcoming OpenRelik to the OSDFIR Infrastructure family",
                 "https://osdfir.blogspot.com/2026/06/welcoming-openrelik-to-osdfir.html"),
                ("How to Use Image Categorization in Oxygen Forensic® Detective",
                 "https://www.oxygenforensics.com/technical-resources/image-categorization/"),
                ("BitLocker Decryption Today: YellowKey Explained and Where Passware Steps In",
                 "https://blog.passware.com/bitlocker-decryption-today-yellowkey/"),
                ("Training Philosophy: Law Enforcement vs. Private Sector",
                 "https://dfirphilosophy.blogspot.com/2026/06/training-philosophy-law-enforcement-vs.html"),
                ("Cross-Org Visibility for LimaCharlie",
                 "https://blog.reconinfosec.com/cross-org-visibility-for-limacharlie"),
                ("A Buffer Is Not a Cure",
                 "https://robtlee73.substack.com/p/a-buffer-is-not-a-cure"),
                ("Sentinel-As-Code: Wave 4, the docs nobody wanted to write",
                 "https://sentinel.blog/sentinel-as-code-wave-4-the-docs-nobody-wanted-to-write/"),
                ("Incident Response Metrics That Actually Matter to Boards (And the Ones That Don’t)",
                 "https://www.sygnia.co/blog/incident-response-metrics-that-matter/"),
                ("Splunk 101: Hands-On Introduction to SIEM, Log Ingestion, and Basic Threat Hunting",
                 "https://systemweakness.com/splunk-101-hands-on-introduction-to-siem-log-ingestion-and-basic-threat-hunting-8324d41c2a01?source=rss----f20a9840e177---4"),
                ("You’ve Got This: Just Hit Submit on That Brilliant Idea",
                 "https://dispatch.thorcollective.com/p/youve-got-this-just-hit-submit-on"),
            ],
        },
        {
            "heading": "SOFTWARE UPDATES",
            "items": [
                ("Malwoverview 8.0.2",
                 "https://github.com/alexandreborges/malwoverview/releases/tag/v8.0.2"),
                ("Jumplist-Browser LNK & Jumplist Browser v.1.0.25",
                 "https://github.com/kacos2000/Jumplist-Browser/releases/tag/v.1.0.25"),
                ("winfor-salt v2026.9.6",
                 "https://github.com/digitalsleuth/winfor-salt/releases/tag/v2026.9.6"),
                ("PolarProxy 2.0.1 Released",
                 "https://www.netresec.com/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released"),
                ("PE-Bear v0.7.2",
                 "https://github.com/hasherezade/pe-bear/releases/tag/v0.7.2"),
                ("SpiceCrypt 3.0: QSPICE Support",
                 "https://jtsylve.blog/post/2026/06/03/spice-crypt-3.0"),
                ("Microsoft-Analyzer-Suite v1.8.0",
                 "https://github.com/LETHAL-FORENSICS/Microsoft-Analyzer-Suite/releases/tag/v1.8.0"),
                ("MISP 2.5.39 – New Dashboard Experience, Stronger STIX, Sharper Analyst Workflows",
                 "https://www.misp-project.org/2026/06/05/misp.2.5.39.released.html/"),
                ("Tool Release – Ghidra MediaTek Modem Image Loader",
                 "https://www.nccgroup.com/research/tool-release-ghidra-mediatek-modem-image-loader/"),
                ("New THOR Cloud Log Inspection View",
                 "https://www.nextron-systems.com/2026/06/02/new-thor-cloud-log-inspection-view/"),
                ("Sedgwick v1.3 Release!",
                 "https://northloopconsulting.com/blog/f/sedgwick-v13-release"),
                ("7.260604.0",
                 "https://github.com/OpenCTI-Platform/opencti/releases/tag/7.260604.0"),
                ("open-investigator Open Investigator v1.26.0",
                 "https://github.com/SEc-123/open-investigator/releases/tag/v1.26.0"),
                ("6.1.6",
                 "https://github.com/radareorg/radare2/releases/tag/6.1.6"),
                ("Velociraptor Release 0.76.6",
                 "https://github.com/Velocidex/velociraptor/releases/tag/v0.76.6"),
                ("YARA v4.5.7",
                 "https://github.com/VirusTotal/yara/releases/tag/v4.5.7"),
            ],
        },
    ],
}


# ── Live feed items (from watchtower.py run 2026-06-09) ───────────────────────
BRUTALIST_ITEMS = [
    ("Infosec News Nuggets — June 8, 2026",
     "https://aboutdfir.com/infosec-news-nuggets-june-8-2026/"),
    ("Infosec News Nuggets — June 5, 2026",
     "https://aboutdfir.com/infosec-news-nuggets-june-5-2026/"),
    ("Infosec News Nuggets — June 4, 2026",
     "https://aboutdfir.com/infosec-news-nuggets-june-4-2026/"),
    ("Infosec News Nuggets — June 2, 2026",
     "https://aboutdfir.com/infosec-news-nuggets-june-2-2026/"),
    ("Leica’s Marcus Rowe On Investigating The World’s Largest Crash Test, Plus What To Expect At FEE 2026",
     "https://www.forensicfocus.com/podcast/leicas-marcus-rowe-on-investigating-the-worlds-largest-crash-test-plus-what-to-expect-at-fee-2026/"),
    ("Forensic Focus Digest, June 05 2026",
     "https://www.forensicfocus.com/news/forensic-focus-digest-june-05-2026/"),
    ("How Freeland Is Using Detego Technology to Dismantle Wildlife Trafficking Networks",
     "https://www.forensicfocus.com/news/how-freeland-is-using-detego-technology-to-dismantle-wildlife-trafficking-networks/"),
    ("Video Timing In Amped FIVE",
     "https://www.forensicfocus.com/articles/video-timing-in-amped-five/"),
    ("Digital Forensics Round-Up, June 03 2026",
     "https://www.forensicfocus.com/news/digital-forensics-round-up-june-03-2026/"),
    ("Andreas Antonsen, Founder, STNDRDS AB",
     "https://www.forensicfocus.com/interviews/andreas-antonsen-founder-stndrds-ab/"),
    ("Burnout, PTSD, Suicidal Thoughts – The DFIR Well-Being Study Results Are In",
     "https://www.forensicfocus.com/podcast/burnout-ptsd-suicidal-thoughts-the-dfir-well-being-study-results-are-in/"),
    ("Forensics StartMe Updates (June 2026)",
     "https://www.stark4n6.com/2026/06/forensics-startme-updates-june-2026.html"),
    ("DFIR+AI Primer: When Not To Use GenAI",
     "https://www.cybertriage.com/ai/dfirai-primer-when-not-to-use-genai/"),
    ("In memoriam Mary Cassatt: 2, 1880-81",
     "https://eclecticlight.co/2026/06/08/in-memoriam-mary-cassatt-2-1880-81/"),
    ("Solutions to Saturday Mac riddles 363",
     "https://eclecticlight.co/2026/06/08/solutions-to-saturday-mac-riddles-363/"),
    ("How does Lockdown Mode affect location data?",
     "https://eclecticlight.co/2026/06/08/how-does-lockdown-mode-affect-location-data/"),
    ("Elihu Vedder’s symbolism and stories: 1885-1913",
     "https://eclecticlight.co/2026/06/07/elihu-vedders-symbolism-and-stories-1885-1913/"),
    ("Last Week on My Mac: What’s in a name?",
     "https://eclecticlight.co/2026/06/07/last-week-on-my-mac-whats-in-a-name/"),
    ("Elihu Vedder’s symbolism and stories: 1863-1884",
     "https://eclecticlight.co/2026/06/06/elihu-vedders-symbolism-and-stories-1863-1884/"),
    ("Saturday Mac riddles 363",
     "https://eclecticlight.co/2026/06/06/saturday-mac-riddles-363/"),
    ("Explainer: Getting a location",
     "https://eclecticlight.co/2026/06/06/explainer-getting-a-location/"),
    ("In the shadow: Introduction",
     "https://eclecticlight.co/2026/06/05/in-the-shadow-introduction/"),
    ("Get more from Get Info and the Finder’s contextual menu",
     "https://eclecticlight.co/2026/06/05/get-more-from-get-info-and-the-finders-contextual-menu/"),
    ("The Duopoly in Digital Forensics",
     "https://www.reddit.com/r/computerforensics/comments/1u0gp3m/the_duopoly_in_digital_forensics/"),
    ("Crow-Eye Release v0.11.0 — Eye AI Compliance & Correlation Engine Upgrade",
     "https://www.reddit.com/r/computerforensics/comments/1tzlfbf/croweye_release_v0110_eye_ai_compliance/"),
    ("Autopsy keyword ingest",
     "https://www.reddit.com/r/computerforensics/comments/1tyn9n9/autopsy_keyword_ingest/"),
    ("Research Notes from Building a Windows Event Log Hunting Workflow",
     "https://www.reddit.com/r/computerforensics/comments/1twhzq9/research_notes_from_building_a_windows_event_log/"),
    ("EDRChoker: Choking The Telemetry Stream to Bypass Defenses",
     "https://www.reddit.com/r/netsec/comments/1tz81jo/edrchoker_choking_the_telemetry_stream_to_bypass/"),
    ("CVE-2026-46640: Developing payloads for Twig sandbox bypass",
     "https://www.reddit.com/r/netsec/comments/1tywxh9/cve202646640_developing_payloads_for_twig_sandbox/"),
    ("Keeping Secrets Out of Logs",
     "https://www.reddit.com/r/netsec/comments/1txmr5f/keeping_secrets_out_of_logs/"),
    ("Unauthenticated RCE as QSECOFR via IBM i Management Central — port 5555, client-controlled verify flag, no credentials required (V7R4 and earlier)",
     "https://www.reddit.com/r/netsec/comments/1txidow/unauthenticated_rce_as_qsecofr_via_ibm_i/"),
    ("System Over Model, Tested: Reproducing Mythos’s FreeBSD Find on Local Open-Weight Models",
     "https://www.reddit.com/r/netsec/comments/1twvplu/system_over_model_tested_reproducing_mythoss/"),
    ("Enter the WasmForge: Compiling Sliver into WebAssembly",
     "https://www.reddit.com/r/netsec/comments/1two9pa/enter_the_wasmforge_compiling_sliver_into/"),
    ("Re:CACHE - Excessive reflection, type confusion, and 0-click SXSS on Next.js",
     "https://www.reddit.com/r/netsec/comments/1twpx2a/recache_excessive_reflection_type_confusion_and/"),
    ("Hacking your PC using your speaker without ever touching it",
     "https://www.reddit.com/r/netsec/comments/1tvlsan/hacking_your_pc_using_your_speaker_without_ever/"),
    ("Interesting- What LLM vuln research looks like",
     "https://www.reddit.com/r/netsec/comments/1tvnz0o/interesting_what_llm_vuln_research_looks_like/"),
    ("Golang code review notes II - elttam",
     "https://www.reddit.com/r/netsec/comments/1tvh7t4/golang_code_review_notes_ii_elttam/"),
    ("1-Click GitHub Token Stealing via a VSCode Bug",
     "https://www.reddit.com/r/netsec/comments/1tuue57/1click_github_token_stealing_via_a_vscode_bug/"),
    ("CTO at NCSC Summary: week ending June 7th",
     "https://www.reddit.com/r/blueteamsec/comments/1tybirs/cto_at_ncsc_summary_week_ending_june_7th/"),
    ("Security Notice: Former Helm APT Mirror Domain `baltocdn.com` Statement",
     "https://www.reddit.com/r/blueteamsec/comments/1u0iwm5/security_notice_former_helm_apt_mirror_domain/"),
    ("HTTP/2 HPACK amplification: detection signatures + the nginx/Apache directives that actually stop it (lab- & vps verified)",
     "https://www.reddit.com/r/blueteamsec/comments/1u0chaa/http2_hpack_amplification_detection_signatures/"),
    ("Z-Jail: A lightweight, multi-layer Linux sandbox combining namespaces, pivot_root, seccomp-bpf, capability dropping, and an evidence-based verdict engine (Truthimatics Public Version) for secure, auditable code execution.",
     "https://www.reddit.com/r/blueteamsec/comments/1tzx123/zjail_a_lightweight_multilayer_linux_sandbox/"),
    ("BusyWork: Replacing Sleep with Real Work to Break Behavioral Detection",
     "https://www.reddit.com/r/blueteamsec/comments/1tzxg3t/busywork_replacing_sleep_with_real_work_to_break/"),
    ("EDRChoker: A tool uses the QoS Policy (Pacer.sys) to throttle Endpoint Detection and Response (EDR) agents from connecting to the server.",
     "https://www.reddit.com/r/blueteamsec/comments/1tzhyo7/edrchoker_a_tool_uses_the_qos_policy_pacersys_to/"),
    ("Query-Hub: CQL Hub is an open repository of detection and hunting queries for CrowdStrike NextGen SIEM and Falcon LogScale.",
     "https://www.reddit.com/r/blueteamsec/comments/1tzxmrw/queryhub_cql_hub_is_an_open_repository_of/"),
    ("Security Review Request — TID Linux Kernel Module",
     "https://www.reddit.com/r/blueteamsec/comments/1tzyeer/security_review_request_tid_linux_kernel_module/"),
    ("Building a safe, effective sandbox to enable Codex on Windows",
     "https://www.reddit.com/r/blueteamsec/comments/1tzy4li/building_a_safe_effective_sandbox_to_enable_codex/"),
    ("About PCIe DMA Cheats: Protocol, IOMMU, Hardware, and Detection",
     "https://www.reddit.com/r/blueteamsec/comments/1tzxgwv/about_pcie_dma_cheats_protocol_iommu_hardware_and/"),
    ("CrowdStrike LogScale queries I use to detect LOLBin- built from 10 years of production SOC work",
     "https://www.reddit.com/r/blueteamsec/comments/1tyvcz0/crowdstrike_logscale_queries_i_use_to_detect/"),
    ("UPnPHostFileRead: Arbitrary file read exploit for the Windows UPnP Device Host service.",
     "https://www.reddit.com/r/blueteamsec/comments/1tzlpu8/upnphostfileread_arbitrary_file_read_exploit_for/"),
    ("The Privileged Roles Nobody Talks About",
     "https://www.reddit.com/r/blueteamsec/comments/1tz4i2r/the_privileged_roles_nobody_talks_about/"),
    ("Sysmon RegistryEvent exclude not overriding include rule for Event ID 13",
     "https://www.reddit.com/r/blueteamsec/comments/1tzarkp/sysmon_registryevent_exclude_not_overriding/"),
    ("Pwnd Blaster: Hacking your PC using your speaker without ever touching it",
     "https://www.reddit.com/r/blueteamsec/comments/1tz7ctw/pwnd_blaster_hacking_your_pc_using_your_speaker/"),
    ("Popping Root on UniFi OS Server: Unauthenticated RCE Chain Detection & Analysis",
     "https://www.reddit.com/r/blueteamsec/comments/1tz42qu/popping_root_on_unifi_os_server_unauthenticated/"),
    ("Inside an Active STX RAT Supply Chain Campaign - A threat actor spent one month building a trojanized software supply chain aimed at a specific type of victim",
     "https://www.reddit.com/r/blueteamsec/comments/1tz4kg7/inside_an_active_stx_rat_supply_chain_campaign_a/"),
    ("Unmasking Quellostanco: How a Git Commit Exposed a Threat Actor Targeting Egyptian Infrastructure (co-authored)",
     "https://www.reddit.com/r/blueteamsec/comments/1tz4iu0/unmasking_quellostanco_how_a_git_commit_exposed_a/"),
    ("Auditing GitLab: The CI/CD Kill Chain - GoGatoZ — a purpose-built Go tool for GitLab CI/CD security auditing that can perform and automate the entire CI/CD kill chain...",
     "https://www.reddit.com/r/blueteamsec/comments/1tz4guk/auditing_gitlab_the_cicd_kill_chain_gogatoz_a/"),
    ("cygor: An modular asset discovery framework written in python to automate the repeating manual work",
     "https://www.reddit.com/r/blueteamsec/comments/1tz78p8/cygor_an_modular_asset_discovery_framework/"),
    ("21 Zero-Days in FFmpeg",
     "https://www.reddit.com/r/blueteamsec/comments/1tz29zm/21_zerodays_in_ffmpeg/"),
    ("On May 31, 2026, Meta discovered that there was a vulnerability in an AI-assisted account recovery system for Instagram (\"High Touch Support\" or \"HTS\") that was exploited byun authorized third parties to perform password resets on Instagram user accounts.",
     "https://www.reddit.com/r/blueteamsec/comments/1tz5q4q/on_may_31_2026_meta_discovered_that_there_was_a/"),
    ("The Detection & Response Chronicles: Covert Operations Through QEMU",
     "https://www.reddit.com/r/blueteamsec/comments/1tyqtq9/the_detection_response_chronicles_covert/"),
    ("Chinese-Cybercrime-Research: Resources to learn more about Chinese-language cybercrime actors.",
     "https://www.reddit.com/r/blueteamsec/comments/1tz589j/chinesecybercrimeresearch_resources_to_learn_more/"),
    ("Fake Interview deploys stealthy cross platform (macOS/Windows) through npm package install in take home assessment",
     "https://www.reddit.com/r/Malware/comments/1u0f2ft/fake_interview_deploys_stealthy_cross_platform/"),
    ("73 Microsoft GitHub repositories impacted by Miasma malware",
     "https://www.reddit.com/r/Malware/comments/1u0304j/73_microsoft_github_repositories_impacted_by/"),
    ("Detecting npm Native Addon Malware: node-gyp Abuse",
     "https://www.reddit.com/r/Malware/comments/1ty7ae6/detecting_npm_native_addon_malware_nodegyp_abuse/"),
    ("Microsoft Warns of GPU Cryptojacking Campaign Spread Through AI Chatbot Links",
     "https://www.reddit.com/r/Malware/comments/1txedfn/microsoft_warns_of_gpu_cryptojacking_campaign/"),
    ("Recommendation",
     "https://www.reddit.com/r/Malware/comments/1tvroif/recommendation/"),
    ("ChatGPT Malvertising Campaign",
     "https://www.reddit.com/r/Malware/comments/1tvsx98/chatgpt_malvertising_campaign/"),
    ("🚨 PCPJack's SMTP Toolkit Dissected: 3 Deployer Generations, Multi-Arch Chisel, and a Full EHLO/STARTTLS Verification Loop",
     "https://www.reddit.com/r/Malware/comments/1tvuxqm/pcpjacks_smtp_toolkit_dissected_3_deployer/"),
    ("LLMShare: using shared chatbot pages to distribute malware",
     "https://www.reddit.com/r/Malware/comments/1tujqkh/llmshare_using_shared_chatbot_pages_to_distribute/"),
    ("We Think the SpaceX IPO Is Overvalued",
     "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued?content_id=20768396545"),
    ("Federal judge blocks H1B visa $100K fee",
     "https://www.alaskasnewssource.com/2026/06/08/federal-judge-blocks-h1-b-visa-100k-fee/"),
    ("Remembering the USS Liberty – and why it still matters",
     "https://captimes.com/opinion/guest-columns/opinion-remembering-the-uss-liberty-and-why-it-still-matters/article_5880cb7e-e863-4c1b-95fb-dfdc5b3e4de2.html"),
    ("Show HN: Mach – A compiled systems language looking for contributions",
     "https://github.com/octalide/mach"),
    ("Show HN: Command Center, the AI coding env for people who care about quality",
     "https://www.cc.dev/"),
    ("OpenAI Submits S-1 Draft to SEC",
     "https://openai.com/index/openai-submits-confidential-s-1/"),
    ("Apple bets cheaper AI will woo small developers",
     "https://techcrunch.com/2026/06/08/apple-bets-cheaper-ai-will-woo-small-developers/"),
    ("FrontierCode",
     "https://cognition.ai/blog/frontier-code"),
    ("I'm building a parallel internet, and it's called The Thinnernet",
     "https://inavoyage.blogspot.com/2026/06/im-building-parallel-internet-and-its.html"),
    ("Surveillance Is Not Safety: A statement on the UK's latest threat to privacy [pdf]",
     "https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf"),
    ("Andrew Tate's Empire of Abuse",
     "https://www.newyorker.com/magazine/2026/06/15/andrew-tates-empire-of-abuse"),
    ("Apple reveals new AI architecture built around Google Gemini models",
     "https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/"),
    ("Why are cells small?",
     "https://burrito.bio/essays/what-limits-a-cells-size"),
    ("Switzerland wil have a referendum to cap population at 10M",
     "https://www.admin.ch/en/sustainability-initiative"),
    ("Apple Core AI Framework",
     "https://developer.apple.com/documentation/coreai/"),
    ("Sam Bankman-Fried applies for a pardon from Trump",
     "https://techcrunch.com/2026/06/08/sam-bankman-fried-applies-for-a-pardon-from-trump/"),
    ("github.com/bryan-ambrose/DFIR_Tools",
     "https://github.com/bryan-ambrose/DFIR_Tools"),
]

# ── Community channels (static) ───────────────────────────────────────────────
COMMUNITY_CHANNELS = [
    {"name":"r/computerforensics","url":"https://www.reddit.com/r/computerforensics/",
     "members":"60k+","color":"#0e7490",
     "description":"Case discussions, tool Q&A, and career advice for digital forensics practitioners."},
    {"name":"r/blueteamsec","url":"https://www.reddit.com/r/blueteamsec/",
     "members":"45k+","color":"#2563eb",
     "description":"High-signal defensive security: threat intel, detection engineering, and incident response links."},
    {"name":"r/netsec","url":"https://www.reddit.com/r/netsec/",
     "members":"500k+","color":"#dc2626",
     "description":"Technical information security content — research papers, exploits, tooling, and write-ups."},
    {"name":"r/Malware","url":"https://www.reddit.com/r/Malware/",
     "members":"85k+","color":"#b45309",
     "description":"Malware analysis, reverse engineering samples, and threat actor discussions."},
    {"name":"r/cybersecurity","url":"https://www.reddit.com/r/cybersecurity/",
     "members":"1M+","color":"#047857",
     "description":"Broad security community: news, certifications, career paths, and industry happenings."},
    {"name":"r/ReverseEngineering","url":"https://www.reddit.com/r/ReverseEngineering/",
     "members":"200k+","color":"#7c3aed",
     "description":"Reversing tools, CTF write-ups, binary analysis, and low-level debugging techniques."},
]

# ── rendering helpers ─────────────────────────────────────────────────────────
def render_week(week_data, is_new=False):
    total = sum(len(s["items"]) for s in week_data["sections"])
    badge = '<span class="badge-new">LATEST</span>' if is_new else ""
    parts = [f"""
  <div class="source-block">
    <div class="week-head">
      <h3><a href="{esc(week_data['url'])}" target="_blank">{esc(week_data['date'])}</a>
        {badge}
      </h3>
      <span class="meta">{total} links</span>
    </div>"""]

    for sec in week_data["sections"]:
        heading = sec["heading"]
        color   = SECTION_COLORS.get(heading, "#475569")
        slug    = cat_slug(heading)
        id_attr = f' id="cat-{slug}"' if is_new else ""
        label   = heading.title().replace(" / ", "/")
        items   = sec["items"]
        parts.append(f"""
    <div class="section-block"{id_attr}>
      <div class="section-head">
        <span class="cat-badge" style="background:{color}20;color:{color};border:1px solid {color}40">{esc(label)}</span>
        <span class="item-count">{len(items)} items</span>
      </div>
      <ul class="link-list">""")
        for title, url in items:
            parts.append(f'        <li><a href="{esc(url)}" target="_blank" rel="noopener">{esc(title)}</a></li>')
        parts.append("      </ul>\n    </div>")

    parts.append("  </div>")
    return "\n".join(parts)


def render_digest():
    # ── nav ──────────────────────────────────────────────────────────────────
    nav_parts = []
    for sec in W_LATEST["sections"]:
        slug  = cat_slug(sec["heading"])
        color = SECTION_COLORS.get(sec["heading"], "#475569")
        label = sec["heading"].title().replace(" / ", "/")
        nav_parts.append(
            f'<a href="#cat-{slug}" style="color:{color};border-bottom:2px solid {color};padding-bottom:2px">{esc(label)}</a>'
        )
    nav_parts.append('<a href="#feed" style="color:var(--mut)">Recent Feed</a>')
    nav_parts.append('<a href="#community" style="color:#f59e0b">Community</a>')
    nav_html = "\n      ".join(nav_parts)

    # ── stats ─────────────────────────────────────────────────────────────────
    total_curated = sum(len(s["items"]) for s in W_LATEST["sections"])
    total_links   = total_curated + len(BRUTALIST_ITEMS)
    num_cats      = len(W_LATEST["sections"])

    # ── digest block ─────────────────────────────────────────────────────────
    week_html = render_week(W_LATEST, is_new=True)

    # ── feed items ───────────────────────────────────────────────────────────
    feed_items_html = "\n".join(
        f'    <li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a></li>'
        for t, u in BRUTALIST_ITEMS
    )

    # ── community cards ──────────────────────────────────────────────────────
    cards_html = "\n".join(
        f"""    <a class="community-card" href="{esc(c['url'])}" target="_blank" rel="noopener"
       style="border-left-color:{c['color']}">
      <div class="cname">{esc(c['name'])}</div>
      <div class="cmembers">{esc(c['members'])} members</div>
      <div class="cdesc">{esc(c['description'])}</div>
    </a>"""
        for c in COMMUNITY_CHANNELS
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>🏰 DFIR Watchtower — {DATE_STR}</title>
<style>
:root{{
  --bg:#0f1117;--s1:#1a1d27;--s2:#22263a;
  --txt:#e2e8f0;--mut:#64748b;--acc:#38bdf8;
  --brd:#2d3748;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:'Inter',system-ui,-apple-system,sans-serif;font-size:14px;line-height:1.6}}
a{{color:var(--acc);text-decoration:none}}
a:hover{{text-decoration:underline}}

/* header */
.site-header{{background:linear-gradient(135deg,#1e293b 0%,#0f172a 100%);border-bottom:1px solid var(--brd);padding:1.5rem 2rem 1.25rem}}
.site-header h1{{font-size:1.65rem;font-weight:800;letter-spacing:-.02em;color:#f8fafc}}
.site-header h1 span{{color:var(--acc)}}
.site-header .tagline{{color:var(--mut);font-size:.8rem;margin-top:.2rem}}

/* stats bar */
.stats-bar{{display:flex;gap:1.5rem;flex-wrap:wrap;padding:.9rem 2rem;background:var(--s1);border-bottom:1px solid var(--brd)}}
.stat{{display:flex;flex-direction:column}}
.stat .val{{font-size:1.3rem;font-weight:700;color:var(--acc);line-height:1}}
.stat .lbl{{font-size:.7rem;color:var(--mut);text-transform:uppercase;letter-spacing:.06em}}

/* sticky nav */
nav{{position:sticky;top:0;z-index:99;background:var(--s1);border-bottom:1px solid var(--brd);padding:.65rem 2rem;display:flex;gap:1.1rem;flex-wrap:wrap;align-items:center}}
nav a{{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;text-decoration:none;transition:opacity .15s;white-space:nowrap}}
nav a:hover{{opacity:.7}}

/* main layout */
main{{max-width:1100px;margin:0 auto;padding:1.5rem 2rem}}

/* blocks */
.source-block{{background:var(--s1);border-radius:12px;padding:1.25rem 1.4rem;margin-bottom:1.5rem;border:1px solid var(--brd)}}
.week-head{{display:flex;align-items:baseline;gap:.75rem;flex-wrap:wrap;margin-bottom:1rem;border-bottom:1px solid var(--brd);padding-bottom:.75rem}}
.week-head h3{{font-size:1.05rem;font-weight:700}}
.week-head h3 a{{color:var(--txt)}}
.week-head h3 a:hover{{color:var(--acc)}}
.meta{{color:var(--mut);font-size:.78rem}}

/* latest badge */
.badge-new{{background:#0e7490;color:#fff;font-size:.62rem;font-weight:700;padding:.15rem .45rem;border-radius:4px;text-transform:uppercase;letter-spacing:.06em;vertical-align:middle;margin-left:.3rem}}

/* section blocks */
.section-block{{margin-bottom:1.1rem}}
.section-head{{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem}}
.cat-badge{{font-size:.7rem;font-weight:700;padding:.2rem .55rem;border-radius:5px;text-transform:uppercase;letter-spacing:.05em}}
.item-count{{font-size:.72rem;color:var(--mut)}}

/* link list */
.link-list{{list-style:none;display:flex;flex-direction:column;gap:.25rem;padding-left:.25rem}}
.link-list li{{border-left:2px solid var(--brd);padding-left:.6rem}}
.link-list li a{{color:#cbd5e1;font-size:.83rem}}
.link-list li a:hover{{color:var(--acc)}}

/* feed section */
#feed .source-block{{background:var(--s2)}}
#feed .link-list li a{{color:#94a3b8}}

/* community */
.community-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:.9rem;margin-top:.75rem}}
.community-card{{background:var(--s1);border-radius:10px;padding:1rem 1.1rem;border-left:4px solid;transition:transform .15s,box-shadow .15s;text-decoration:none;display:block}}
.community-card:hover{{transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,0,0,.4)}}
.community-card .cname{{font-weight:700;font-size:.95rem;color:var(--acc);margin-bottom:.25rem}}
.community-card .cmembers{{font-size:.7rem;color:var(--mut);margin-bottom:.4rem}}
.community-card .cdesc{{font-size:.82rem;color:var(--txt);line-height:1.45}}

/* section headers */
.section-title{{font-size:.95rem;font-weight:700;color:var(--mut);text-transform:uppercase;letter-spacing:.08em;margin:2rem 0 .75rem;padding-bottom:.4rem;border-bottom:1px solid var(--brd)}}

footer{{text-align:center;padding:2rem;color:var(--mut);font-size:.75rem;border-top:1px solid var(--brd);margin-top:2rem}}
</style>
</head>
<body>

<header class="site-header">
  <h1>🏰 DFIR <span>Watchtower</span></h1>
  <div class="tagline">Weekly intelligence digest for digital forensics &amp; incident response professionals</div>
</header>

<div class="stats-bar">
  <div class="stat"><span class="val">{total_links}</span><span class="lbl">Total Links</span></div>
  <div class="stat"><span class="val">{total_curated}</span><span class="lbl">Curated Links</span></div>
  <div class="stat"><span class="val" style="font-size:.85rem">{W_LATEST["date"]}</span><span class="lbl">Edition</span></div>
  <div class="stat"><span class="val">{num_cats}</span><span class="lbl">Categories</span></div>
  <div class="stat"><span class="val" style="font-size:.85rem">{PULL_TIME}</span><span class="lbl">Pulled</span></div>
</div>

<nav>
  {nav_html}
</nav>

<main>
  <div class="section-title">📋 Curated Intelligence</div>
  {week_html}

  <div class="section-title" id="feed">⚡ Recent Tech &amp; Security Feed</div>
  <div class="source-block" id="feed-block">
    <ul class="link-list">
{feed_items_html}
    </ul>
  </div>

  <div class="section-title" id="community-label">🛡️ Community Channels</div>
  <div class="source-block" id="community">
    <div class="week-head" style="margin-bottom:.75rem">
      <h3>Community Channels</h3>
      <span class="meta">DFIR &amp; security subreddits worth following</span>
    </div>
    <div class="community-grid">
{cards_html}
    </div>
  </div>
</main>

<footer>🏰 DFIR Watchtower — {PULL_TIME} — github.com/forensicfellowship/DFIR_Watchtower</footer>

</body>
</html>"""

# ── write output ──────────────────────────────────────────────────────────────
base = Path(__file__).parent
content = render_digest()
out_dated = base / f"watchtower_digest_{DATE_STR}.html"
out_index = base / "index.html"

out_dated.write_text(content, encoding="utf-8")
out_index.write_text(content, encoding="utf-8")

total_curated = sum(len(s["items"]) for s in W_LATEST["sections"])
total_links   = total_curated + len(BRUTALIST_ITEMS)
print(f"✅  Wrote {out_dated.name} ({len(content):,} bytes)")
print(f"✅  Wrote index.html")
print(f"📊  {total_curated} curated + {len(BRUTALIST_ITEMS)} feed = {total_links} total links")
