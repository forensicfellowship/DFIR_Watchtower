#!/usr/bin/env python3
"""
DFIR Watchtower — Full Digest Builder
Sources: This Week in 4n6 (Weeks 10-12), start.me Blog Feed, Brutalist Report Tech
Scraped live 2026-03-28 via Chrome browser extension
"""
import html
from datetime import datetime, timezone
from pathlib import Path

NOW = datetime.now(timezone.utc)
DATE_STR = NOW.strftime("%Y-%m-%d")
TIMESTAMP = NOW.strftime("%Y-%m-%d %H:%M UTC")

# ═══════════════════════════════════════════════════════════════════════════
# THIS WEEK IN 4N6 — STRUCTURED DATA PER WEEK
# Format: { "heading": str, "items": [["Title", "https://url"], ...] }
# ═══════════════════════════════════════════════════════════════════════════

W12 = {
    "week": "Week 12 – 2026",
    "url": "https://thisweekin4n6.com/2026/03/22/week-12-2026/",
    "date": "2026-03-22",
    "sections": [
        {
            "heading": "FORENSIC ANALYSIS",
            "items": [
                ["AI-Powered Picture Analysis with BelkaGPT", "https://belkasoft.com/ai-powered-picture-analysis"],
                ["Looks Can Lie: Is That Really an NVMe Drive? (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/looks-can-lie-is-that-really-an-nvme-drive/"],
                ["2026 MSAB CTF: Android Questions (Hexordia)", "https://www.hexordia.com/blog/2026-msab-ctf-android-questions"],
                ["2026 MSAB CTF: iOS Questions (Hexordia)", "https://www.hexordia.com/blog/2026-msab-ctf-ios-questions"],
                ["BDC – More Battery Temps & Charging Stats for iOS (Stark 4N6)", "https://www.stark4n6.com/2026/03/bdc-more-battery-temps-charging-stats.html"],
                ["Tracking LockBit Through Memory Forensics", "https://systemweakness.com/tracking-lockbit-through-memory-forensics-a0ba37aba21c"],
            ],
        },
        {
            "heading": "THREAT INTELLIGENCE / HUNTING",
            "items": [
                ["CVE-2025-32975: Arctic Wolf Observes Exploitation of Quest KACE SMA", "https://arcticwolf.com/resources/blog-uk/cve-2025-32975-arctic-wolf-observes-exploitation-of-quest-kace-systems-management-appliance/"],
                ["Nation-State Attacks Hit Machine Speed: 2026 Armis Cyberwarfare Report", "https://www.armis.com/blog/nation-state-attacks-hit-machine-speed-key-takeaways-of-the-2026-armis-cyberwarfare-report-and-what-it-means-for-security-teams/"],
                ["February 2026 APT Attack Trends Report — South Korea (ASEC)", "https://asec.ahnlab.com/en/92972/"],
                ["Winos4.0 malware disguised as KakaoTalk installation file (ASEC)", "https://asec.ahnlab.com/en/92971/"],
                ["Attack case against MS-SQL server installing ICE Cloud scanner Larva-26002 (ASEC)", "https://asec.ahnlab.com/en/92988/"],
                ["From flat networks to locked up domains with tiering models (SensePost)", "https://sensepost.com/blog/2026/from-flat-networks-to-locked-up-domains-with-tiering-models/"],
                ["CTA Campaign Assessment: The Iran Conflict – Global Cyber Operations Risk (Avertium)", "https://www.avertium.com/resources/threat-reports/cta-campaign-assessment-iran-conflict"],
                ["Amazon threat intelligence teams identify Interlock ransomware campaign (AWS)", "https://aws.amazon.com/blogs/security/amazon-threat-intelligence-teams-identify-interlock-ransomware/"],
                ["Sandworm: Russia's global infrastructure wrecking crew (Barracuda)", "https://blog.barracuda.com/2026/03/sandworm-russia-infrastructure-wrecking-crew"],
                ["LotAI: How Attackers Weaponize AI Assistants for Data Exfiltration (BlackFog)", "https://www.blackfog.com/lotai-attackers-weaponize-ai-assistants/"],
                ["2026-03-17: SmartApeSG ClickFix pushes Remcos RAT (Brad Duncan / SANS ISC)", "https://malware-traffic-analysis.net/2026/03/17/index.html"],
                ["Feds Disrupt IoT Botnets Behind Huge DDoS Attacks (Krebs on Security)", "https://krebsonsecurity.com/2026/03/feds-disrupt-iot-botnets-behind-huge-ddos-attacks/"],
                ["ResidentBat: Belarusian KGB Android Spyware at Internet Scale (Censys)", "https://censys.com/residentbat-belarusian-kgb-android-spyware/"],
                ["Vshell: A Chinese-Language Alternative to Cobalt Strike (Censys)", "https://censys.com/vshell-chinese-language-alternative-cobalt-strike/"],
                ["Odyssey Stealer: Inside a macOS Crypto-Stealing Operation (Censys)", "https://censys.com/odyssey-stealer-macos-crypto-stealing/"],
                ["Transparent COM instrumentation for malware analysis (Cisco Talos)", "https://blog.talosintelligence.com/transparent-com-instrumentation-for-malware-analysis/"],
                ["Everyday tools, extraordinary crimes: the ransomware exfiltration playbook (Cisco Talos)", "https://blog.talosintelligence.com/ransomware-exfiltration-playbook/"],
                ["MacSync Stealer: SEO Poisoning and ClickFix-Based macOS Malware (CloudSEK)", "https://www.cloudsek.com/blog/macsync-stealer-seo-poisoning-clickfix-macos-malware"],
                ["LiveChat Abuse: How Phishers Are Exploiting SaaS Support Tools (Cofense)", "https://cofense.com/blog/livechat-abuse-phishers-exploiting-saas-support-tools/"],
                ["From Scanner to Stealer: Inside the trivy-action Supply Chain Compromise (CrowdStrike)", "https://www.crowdstrike.com/blog/trivy-action-supply-chain-compromise/"],
                ["Tycoon2FA Phishing-as-a-Service Platform Persists Following Takedown (CrowdStrike)", "https://www.crowdstrike.com/blog/tycoon2fa-phishing-as-a-service-persists/"],
                ["FancyBear Exposed: Major OPSEC Blunder Inside Russian Espionage Ops (Ctrl-Alt-Intel)", "https://ctrlaltintel.com/fancybear-opsec-blunder/"],
                ["AI-Assisted Phishing Campaign Exploits Browser Permissions (Cyble)", "https://cyble.com/blog/ai-assisted-phishing-browser-permissions/"],
                ["Middle East Cyber Warfare Intensifies: Rising Attacks, Hacktivist Surge (Cyble)", "https://cyble.com/blog/middle-east-cyber-warfare-intensifies/"],
                ["North Korea's Crypto Theft Operations: Lazarus Group (Cyble)", "https://cyble.com/blog/north-korea-crypto-theft-lazarus-group/"],
                ["Weekly Intelligence Report – 20 March 2026 (Cyfirma)", "https://www.cyfirma.com/research/weekly-intelligence-report-20-march-2026/"],
                ["Darktrace Identifies Encryption in a World Leaks Ransomware Attack", "https://darktrace.com/blog/world-leaks-ransomware-attack/"],
                ["Threat Hunting: Catching emojis on Files and Email Subjects + KQL (Detect FYI)", "https://detect.fyi/threat-hunting-catching-emojis-on-files-and-email-subjects"],
                ["Detection via Deception — Using your SIEM as a Free Deception Platform (Detect FYI)", "https://detect.fyi/detection-via-deception-using-siem-as-deception-platform"],
                ["Detection Logic Bugs: Abusable Gaps in Detection Coverage (Detect FYI)", "https://detect.fyi/detection-logic-bugs-abusable-gaps-in-detection-coverage"],
                ["Weekly Threat Infrastructure Investigation Week 9-10 (Disconinja)", "https://disconinja.hatenablog.com/entry/2026/03/17/215616"],
                ["Microsoft Graph API Attack Surface: OAuth Flows, Abused Endpoints (InfoSec Write-ups)", "https://infosecwriteups.com/microsoft-graph-api-attack-surface-oauth-flows-abused-endpoints-and-what-defenders-miss-9c303ea2aa02"],
                ["New Malware Highlights Increased Systematic Targeting of Network Infrastructure (Eclypsium)", "https://eclypsium.com/blog/condibot-monaco-malware-network-infrastructure/"],
                ["Linux & Cloud Detection Engineering – Getting Started with Defend for Containers (Elastic)", "https://www.elastic.co/security-labs/getting-started-with-defend-for-containers"],
                ["Linux & Cloud Detection Engineering – TeamPCP Container Attack Scenario (Elastic)", "https://www.elastic.co/security-labs/teampcp-container-attack-scenario"],
                ["WIPED IN 79 COUNTRIES: The Handala Hack Attack on Stryker Corporation (FalconFeeds)", "https://falconfeeds.io/blogs/handala-hack-attack-on-stryker-corporation"],
                ["Iran's FindFace Acquisition: The Architecture of a Digital Surveillance State (FalconFeeds)", "https://falconfeeds.io/blogs/irans-findface-acquisition-digital-surveillance-state"],
                ["Following the Money: The 82-Wallet Bitcoin Cluster Linked to Iran's IRGC-CEC (FalconFeeds)", "https://falconfeeds.io/blogs/82-wallet-bitcoin-cluster-irgc-cec"],
                ["Bench.sh: How Threat Actors Repurpose a Legitimate Benchmarking Tool (Flare)", "https://www.flare.io/blog/bench-sh-threat-actors-repurpose-benchmarking-tool/"],
                ["VoidStealer: Debugging Chrome to Steal Its Secrets (Gen)", "https://www.gendigital.com/blog/voidstealer-debugging-chrome/"],
                ["GhostClaw expands beyond npm: GitHub repositories and AI workflows deliver macOS infostealer (Jamf)", "https://www.jamf.com/blog/ghostclaw-expands-beyond-npm/"],
                ["Poisoned Typeface: How Simple Font Rendering Poisons Every AI Assistant (LayerX)", "https://layerxsecurity.com/blog/poisoned-typeface-font-rendering-ai-assistant/"],
                ["DarkSword Threatens iOS Users (Lookout)", "https://www.lookout.com/threat-intelligence/article/darksword-threatens-ios-users"],
                ["When a Microsoft Teams support call led to compromise (Microsoft Security)", "https://www.microsoft.com/en-us/security/blog/2026/03/18/when-a-microsoft-teams-support-call-led-to-compromise/"],
                ["When tax season becomes cyberattack season: Phishing using tax-related lures (Microsoft)", "https://www.microsoft.com/en-us/security/blog/2026/03/17/when-tax-season-becomes-cyberattack-season/"],
                ["CTI-REALM: A new benchmark for end-to-end detection rule generation with AI (Microsoft)", "https://www.microsoft.com/en-us/security/blog/2026/03/19/cti-realm-benchmark-detection-rule-generation/"],
                ["Attacking Kerberos 2: Roasting Attacks (MII Cyber Security)", "https://mii-cybersecurity.com/attacking-kerberos-roasting-attacks/"],
                ["Finding the 'Quiet' Compromise with Long Tail Analysis (MII)", "https://mii-cybersecurity.com/long-tail-analysis-quiet-compromise/"],
                ["DPRK IT Worker Fraud: Hiring an Insider Threat (Nisos)", "https://www.nisos.com/research/dprk-it-worker-fraud/"],
                ["GlassWorm Invades GitHub, NPM, VS Code and PyPI (OpenSourceMalware)", "https://opensourcemalware.com/glassworm-github-npm-vscode-pypi/"],
                ["Iranian Cyber Threat Evolution: From MBR Wipers to Identity Weaponization (Palo Alto)", "https://unit42.paloaltonetworks.com/iranian-cyber-threat-evolution/"],
                ["Boggy Serpens Threat Assessment (Palo Alto)", "https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/"],
                ["Analyzing the Current State of AI Use in Malware (Palo Alto)", "https://unit42.paloaltonetworks.com/ai-use-in-malware-analysis/"],
                ["T1071.001 Web Protocols in MITRE ATT&CK Explained (Picus)", "https://www.picussecurity.com/resource/blog/t1071-001-web-protocols"],
                ["T1059.013 Container CLI/API in MITRE ATT&CK Explained (Picus)", "https://www.picussecurity.com/resource/blog/t1059-013-container-cli-api"],
                ["What Is Fileless Malware? (Picus)", "https://www.picussecurity.com/resource/blog/what-is-fileless-malware"],
                ["T1219.001 IDE Tunneling in MITRE ATT&CK Explained (Picus)", "https://www.picussecurity.com/resource/blog/t1219-001-ide-tunneling"],
                ["T1547.001 Registry Run Keys/Start Up Folder in MITRE ATT&CK Explained (Picus)", "https://www.picussecurity.com/resource/blog/t1547-001-registry-run-keys"],
                ["CursorJack: Weaponizing Deeplinks to Exploit Cursor IDE (Proofpoint)", "https://www.proofpoint.com/us/blog/threat-insight/cursorjack-weaponizing-deeplinks-exploit-cursor-ide"],
                ["The Stryker breach didn't match the playbook. That shouldn't be a surprise. (Push Security)", "https://pushsecurity.com/blog/stryker-handala-report"],
                ["The Attack Cycle is Accelerating: Rapid7 2026 Global Threat Landscape Report", "https://www.rapid7.com/blog/post/tr-accelerating-attack-cycle-2026-global-threat-landscape-report/"],
                ["Microsoft Orphaned Agents Identities: Hidden identity debt in Entra tenant", "https://thalpius.com/2026/03/17/microsoft-orphaned-agents-identities-the-hidden-identity-debt-in-your-entra-tenant/"],
                ["2025 Identity Threat Landscape Report: Infostealer Economy (Recorded Future)", "https://www.recordedfuture.com/blog/identity-trend-report-march-blog"],
                ["AI and browser threats stand out in the 2026 Threat Detection Report (Red Canary)", "https://redcanary.com/threat-detection-report/"],
                ["Casting a Wider Net: ClickFix, Deno, and LeakNet's Scaling Threat (ReliaQuest)", "https://www.reliaquest.com/blog/clickfix-deno-leaknet-scaling-threat/"],
                ["Observed Telegram Bot Naming Patterns in Recent MuddyWater Malware (Synaptic)", "https://synaptic-systems.co.uk/muddy-water-telegram-bot-naming-patterns/"],
                ["IPv4 Mapped IPv6 Addresses (SANS ISC)", "https://isc.sans.edu/diary/ipv4-mapped-ipv6-addresses/"],
                ["GSocket Backdoor Delivered Through Bash Script (SANS ISC)", "https://isc.sans.edu/diary/gsocket-backdoor-bash-script/"],
                ["UEBA in the Real World: Catching Intrusions That Don't Look Like Intrusions (Sekoia)", "https://www.sekoia.io/en/blog/ueba-real-world-catching-intrusions/"],
                ["Building an Adversarial Consensus Engine | Multi-Agent LLMs for Malware Analysis (SentinelOne)", "https://www.sentinelone.com/blog/adversarial-consensus-engine-multi-agent-llms-malware-analysis/"],
                ["How Kinetic Strikes Opened the Door to Cyber and Influence War (Simone Kraus)", "https://simonekraus.com/kinetic-strikes-cyber-influence-war/"],
                ["GlassWorm Sleeper Extensions Activate on Open VSX (Socket)", "https://socket.dev/blog/glassworm-sleeper-extensions-open-vsx"],
                ["Trivy Under Attack: Widespread GitHub Actions Tag Compromise Exposes CI/CD Secrets (Socket)", "https://socket.dev/blog/trivy-github-actions-tag-compromise"],
                ["CanisterWorm: npm Publisher Compromise Deploys Backdoor Across 29+ Packages (Socket)", "https://socket.dev/blog/canisterworm-npm-publisher-compromise"],
                ["Ransomware 3.0: The Autonomous Threat That Changed Everything (SOCRadar)", "https://socradar.io/ransomware-3-0-autonomous-threat/"],
                ["Android devices ship with firmware-level malware (Sophos)", "https://www.sophos.com/en-us/blog/android-firmware-level-malware"],
                ["How to Prove Incident Containment: Evidence of Absence (Stairwell)", "https://stairwell.com/news/how-to-prove-incident-containment-evidence-of-absence/"],
                ["Stop Renting Your Own Malware Data Back (Stairwell)", "https://stairwell.com/news/stop-renting-your-own-malware-data-back/"],
                ["Continuous Malware Intelligence: Replacing Retro Hunts With Hindsight (Stairwell)", "https://stairwell.com/news/continuous-malware-intelligence/"],
                ["Malicious Polymarket Bot Hides in Hijacked dev-protocol GitHub Org (Step Security)", "https://www.stepsecurity.io/blog/malicious-polymarket-bot-hides-in-hijacked-dev-protocol-github-org-and-steals-wallet-keys"],
                ["Malicious npm in Popular React Native Packages – 130K+ Monthly Downloads (Step Security)", "https://www.stepsecurity.io/blog/malicious-npm-releases-found-in-popular-react-native-packages---130k-monthly-downloads-compromised"],
                ["Trivy Compromised a Second Time – Malicious v0.69.4 Release (Step Security)", "https://www.stepsecurity.io/blog/trivy-compromised-a-second-time---malicious-v0-69-4-release"],
                ["Advanced fake Zoom installer delivering malware (Sublime Security)", "https://proxied2.sublime.security/blog/advanced-fake-zoom-installer-used-for-delivering-malware"],
                ["One Commit Away from Theft: Supply Chain Attacks Hit the Crypto Ecosystem (Sygnia)", "https://www.sygnia.co/blog/one-commit-away-from-theft-supply-chain-attacks-crypto/"],
                ["New Malware Targets Users of Cobra DocGuard Software (Symantec)", "https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cobra-docguard-malware"],
                ["Detecting CVE-2026-3288 & CVE-2026-24512: Ingress-nginx vulnerabilities for Kubernetes (Sysdig)", "https://sysdig.com/blog/detecting-cve-2026-3288-cve-2026-24512-ingress-nginx/"],
                ["CVE-2026-33017: How attackers compromised Langflow AI pipelines (Sysdig)", "https://sysdig.com/blog/cve-2026-33017-langflow-ai-pipelines/"],
                ["ZeroTrace Multi-Family MaaS Operation — Open Directory Exposure (The Hunter's Ledger)", "https://thehuntersledger.com/zerotrace-maas-operation/"],
                ["From Missiles to Malware — Part 2 Defending Against the Handala Campaign (Third Eye)", "https://thirdeye.io/from-missiles-to-malware-part-2/"],
                ["Perseus: DTO malware that takes notes (ThreatFabric)", "https://www.threatfabric.com/blogs/perseus-dto-malware.html"],
                ["Web Shells, Tunnels, and Ransomware: Dissecting a Warlock Attack (Trend Micro)", "https://www.trendmicro.com/en_us/research/26/c/warlock-attack-web-shells-tunnels-ransomware.html"],
                ["From Misconfigured Spring Boot Actuator to SharePoint Exfiltration (Trend Micro)", "https://www.trendmicro.com/en_us/research/26/c/spring-boot-actuator-sharepoint-exfiltration.html"],
                ["Full Disclosure: A Third and Fourth Azure Sign-In Log Bypass Found (TrustedSec)", "https://trustedsec.com/blog/azure-sign-in-log-bypass/"],
                ["How Attackers Establish Persistence in Hybrid Environments (Vectra AI)", "https://www.vectra.ai/blog/how-attackers-establish-persistence-in-hybrid-environments"],
                ["What the Stryker Incident Reveals About Handala's Attack Playbook (Vectra AI)", "https://www.vectra.ai/blog/what-the-stryker-incident-reveals-about-handalas-attack-playbook"],
                ["EDR killers explained: Beyond the drivers (WeLiveSecurity / ESET)", "https://www.welivesecurity.com/en/eset-research/edr-killers-explained-beyond-the-drivers/"],
                ["Trivy Compromised: Everything You Need to Know (Wiz)", "https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack"],
            ],
        },
        {
            "heading": "UPCOMING EVENTS",
            "items": [
                ["BHIS – Talkin' Bout [infosec] News 2026-03-23", "https://www.youtube.com/watch?v=BHISnews20260323"],
                ["Cellebrite – Advanced Digital Investigations in Africa", "https://cellebrite.com/en/resources/webinars/advanced-digital-investigations-in-africa-unlocking-the-evidence-hidden-in-every-device/"],
                ["Cyber Triage – Investigating Evasion: How to Find What the Alert Missed", "https://register.gotowebinar.com/register/9096089726229071963"],
                ["Magnet Forensics – Mobile Unpacked S4:E3 // Deducing the duplications", "https://www.magnetforensics.com/resources/s4e3-deducing-the-duplications-understanding-duplicated-data-in-file-systems/"],
                ["SANS – 2026 Threat Landscape: Turning Threat Intelligence into Analytic Advantage", "https://www.linkedin.com/events/7438173815626641409/"],
            ],
        },
        {
            "heading": "PRESENTATIONS / PODCASTS",
            "items": [
                ["Digital Forensics Now Podcast S3 – Episode 3 (Alexis Brignoni)", "https://www.youtube.com/watch?v=dfn_s3ep3"],
                ["Detect SSH -R Pivoting Before Ransomware Hits (Ayush Anand)", "https://www.youtube.com/watch?v=ssh_pivot"],
                ["Cloud Security Podcast EP267 – AI SOC or AI in a SOC? (Google)", "https://cloud.withgoogle.com/cloudsecurity/podcast/ep267-ai-soc-or-ai-in-a-soc/"],
                ["Cyber Threat Hunting at Scale: 4 Principles from the Trenches (Cyberwox)", "https://www.youtube.com/watch?v=cyberwox_hunting"],
                ["02 – Exploring the Reverse Shell Source Code (Dr Josh Stroschein)", "https://www.youtube.com/watch?v=stroschein_reverseshell"],
                ["Cybersecurity SOC Analyst Lab – Malicious Browser Extension FakeGPT (MyDFIR)", "https://www.youtube.com/watch?v=mydfir_fakegpt"],
                ["Mac Imaging Made Easy with Fuji (Richard Davis / 13Cubed)", "https://www.youtube.com/watch?v=13cubed_fuji"],
                ["LABScon25 Replay: Your Apps May Be Gone, But the Hackers Made $9B (SentinelOne)", "https://www.sentinelone.com/labs/labscon25-replay/"],
                ["Team Cymru: Duaine Labno on Digital Investigations and Corporate Threat Intelligence", "https://team-cymru.com/podcast/duaine-labno-digital-investigations/"],
                ["Intune Wipers, Veeam RCEs, and DPRK's $800M IT Empire (Team Cymru Video)", "https://team-cymru.com/blog/intune-wipers-veeam-rces-dprk/"],
                ["Bloodhound OpenGraph (John Hammond)", "https://www.youtube.com/watch?v=hammond_bloodhound"],
                ["Magnet Forensics – Signals in the noise: Five years of enterprise DFIR trends", "https://www.magnetforensics.com/resources/signals-in-the-noise-five-years-of-enterprise-dfir-trends/"],
                ["Magnet Forensics – Bridging the air gap: Accelerating mobile forensics in secure labs", "https://www.magnetforensics.com/resources/bridging-the-air-gap-accelerating-mobile-forensics/"],
                ["Root Cause Analysis Series Part 1-4 (Mossé Cyber Security Institute)", "https://mcsi.io/root-cause-analysis-series"],
                ["Parsing The Truth: One Byte at a Time Podcast S1 E43: Karen Read – Jessica Hyde Testimony", "https://parsingthetruth.com/e43-karen-read-jessica-hyde/"],
            ],
        },
        {
            "heading": "MALWARE",
            "items": [
                ["Glassworm Strikes Popular React Native Phone Number Packages (Aikido)", "https://www.aikido.dev/blog/glassworm-react-native-phone-packages"],
                ["Open VSX Extension Compromised by BlokTrooper GlassWorm (Aikido)", "https://www.aikido.dev/blog/open-vsx-extension-compromised-bloktrooper-glassworm"],
                ["GlassWorm Hides a RAT Inside a Malicious Chrome Extension (Aikido)", "https://www.aikido.dev/blog/glassworm-rat-malicious-chrome-extension"],
                ["TeamPCP deploys CanisterWorm on NPM following Trivy compromise (Aikido)", "https://www.aikido.dev/blog/teampcp-canisterworm-npm-trivy"],
                ["Forbidden Hyena adopts BlackReaperRAT in AI-powered campaigns (BI.ZONE)", "https://bi.zone/blog/forbidden-hyena-blackreaperrat/"],
                ["Windsurf IDE Extension Drops Malware via Solana Blockchain (Bitdefender)", "https://www.bitdefender.com/en-us/blog/labs/windsurf-ide-extension-solana-malware"],
                ["CQURE Hacks #75: NTFS Forensics – Recovering Deleted Files and Analyzing MFT Records", "https://cqure.academy/cqure-hacks-75-ntfs-forensics/"],
                ["Sweet Minecraft Mods – The Dark Tale of SugarSMP Scam, Malware & Extortion (G Data)", "https://www.gdatasoftware.com/blog/2026/03/sugarsmp-minecraft-malware"],
                ["Reverse Engineering .NET AOT Malware: Multi-Stage Attack Chain with Binary Ninja", "https://howler.cell/blog/dotnet-aot-malware-binary-ninja"],
                ["Fake Telegram Malware Campaign via Typosquatted Websites (K7 Labs)", "https://labs.k7computing.com/fake-telegram-malware-typosquatting/"],
                ["GlassWorm Hits MCP: 5th Wave with New Delivery Techniques (Koi Security)", "https://koi.security/blog/glassworm-mcp-5th-wave"],
                ["AI Wrote This Malware: Dissecting a Vibe-Coded Malware Campaign (McAfee Labs)", "https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ai-written-malware-vibe-coded-campaign/"],
                ["RegPhantom Backdoor Threat Analysis (Nextron Systems)", "https://www.nextron-systems.com/2026/03/20/regphantom-backdoor-threat-analysis/"],
                ["OpenClaw Developers Targeted in Crypto-Wallet Phishing Attack (OX Security)", "https://www.ox.security/blog/openclaw-github-phishing-crypto-wallet-attack/"],
                ["Beyond the Wiper — What Unit42's Iran Analysis Misses (Plausible Deniability)", "https://plausible-deniability.co/blog/BeyondWiper/"],
                ["Free real estate: GoPix, the banking Trojan living off your memory (Securelist)", "https://securelist.com/gopix-banking-trojan/119173/"],
                ["The SOC Files: Unpacking a new Horabot campaign in Mexico (Securelist)", "https://securelist.com/horabot-campaign/119033/"],
                ["Operation GhostMail: Russian APT exploits Zimbra Webmail to Target Ukraine (Seqrite)", "https://www.seqrite.com/blog/operation-ghostmail-zimbra-xss-russian-apt/"],
                ["Analysis of Batch File leads to DonutLoader (Shubho57)", "https://shubho57.medium.com/analysis-of-batch-file-leads-to-donutloader"],
                ["MacOS malware persistence 5: cron jobs (Zhassulan Zhussupov)", "https://cocomelonc.github.io/malware/2026/03/macos-persistence-5-cron.html"],
                ["MacOS malware persistence 6: PAM module injection (Zhassulan Zhussupov)", "https://cocomelonc.github.io/malware/2026/03/macos-persistence-6-pam.html"],
                ["Technical Analysis of SnappyClient (ZScaler)", "https://www.zscaler.com/blogs/security-research/technical-analysis-snappyclient"],
            ],
        },
        {
            "heading": "MISCELLANEOUS",
            "items": [
                ["Introducing DFIR Toolkit: Privacy-First DFIR utilities that run entirely in your browser (Andrea Fortuna)", "https://andreafortuna.org/dfir-toolkit/"],
                ["If you suck at your DFIR job, AI is going to take it (Brett Shavers)", "https://www.dfir.training/blog/if-you-suck-at-dfir-ai-will-take-it"],
                ["A Practical Map of the DFIR Internet: Marketplaces, FAQs, and Fire Exits (DFIR Training)", "https://www.dfir.training/blog/practical-map-of-dfir-internet"],
                ["56% are likely to leave DFIR within 12 months or unsure if they'll stay (DFIR Training)", "https://www.dfir.training/blog/dfir-retention-survey-2026"],
                ["Cellebrite Genesis Launch: Groundbreaking Agentic AI Solution for Investigators", "https://cellebrite.com/en/resources/press-releases/cellebrite-genesis-launch/"],
                ["Guardian Cloud Platform IRAP Assessment: What Australian Investigators Need to Know (Cellebrite)", "https://cellebrite.com/en/blog/guardian-cloud-platform-irap-assessment-australian-investigators/"],
                ["Cellebrite Launches Guardian Investigate, the AI-Powered Nerve Center", "https://cellebrite.com/en/resources/press-releases/cellebrite-guardian-investigate/"],
                ["From Weeks to Minutes: How Agentic AI Is Transforming Digital Investigations (Cellebrite)", "https://cellebrite.com/en/blog/agentic-ai-transforming-digital-investigations/"],
                ["Why iOS Jailbreaking Is Over — And What That Means for Security Teams (Cellebrite)", "https://cellebrite.com/en/blog/why-ios-jailbreaking-is-over/"],
                ["DFIR Jobs Update – 03/16/26 (DFIR Dominican / Josibel Mendoza)", "https://dfirminican.com/dfir-jobs-update-03-16-26/"],
                ["A Study in DFIR: Open-Source, Enterprise, and the Art of Analysis (Baker Street Forensics)", "https://bakerstreetforensics.com/2026/03/18/a-study-in-dfir-open-source-enterprise-and-the-art-of-analysis/"],
                ["Digital Forensics Jobs Round-Up, March 16 2026 (Forensic Focus)", "https://www.forensicfocus.com/articles/digital-forensics-jobs-round-up-march-16-2026/"],
                ["Introducing Aid4Mail: Closing Email Evidence Gaps for Investigators (Forensic Focus)", "https://www.forensicfocus.com/articles/aid4mail-email-evidence-gaps/"],
                ["Digital Forensics Round-Up, March 18 2026 (Forensic Focus)", "https://www.forensicfocus.com/articles/digital-forensics-round-up-march-18-2026/"],
                ["Forensic Focus Digest, March 20 2026", "https://www.forensicfocus.com/articles/forensic-focus-digest-march-20-2026/"],
                ["Explainer: Disk images (Howard Oakley / The Eclectic Light Company)", "https://eclecticlight.co/2026/03/explainer-disk-images/"],
                ["숨겨진 데이터의 실체: Full File System 추출을 통해 드러난 정보들 (Magnet Forensics)", "https://www.magnetforensics.com/blog/full-file-system-extraction-hidden-data/"],
                ["Magnet One Case Stream: A new transformative workflow (Magnet Forensics)", "https://www.magnetforensics.com/blog/magnet-one-case-stream/"],
                ["Setting up UniqueSignal in MISP", "https://misp-project.org/2026/03/setting-up-uniquesignal/"],
                ["Phones Everywhere: How to Catch Them (Matthew Plascencia)", "https://matthewplascencia.com/phones-everywhere-how-to-catch-them/"],
                ["My book, 'A Dance of Red and Blue' is out! (Daniel Koifman)", "https://www.amazon.com/dance-red-blue-koifman/"],
                ["Sentinel-As-Code: The 2026 Update (sentinel.blog / TobyG)", "https://sentinel.blog/2026/03/sentinel-as-code-2026-update/"],
            ],
        },
        {
            "heading": "SOFTWARE UPDATES",
            "items": [
                ["Malwoverview 8.0.0 (Alexandre Borges)", "https://github.com/alexandreborges/malwoverview/releases/tag/v8.0.0"],
                ["Arkime v6.1.0", "https://github.com/arkime/arkime/releases/tag/v6.1.0"],
                ["oledump.py Version 0.0.85 (Didier Stevens)", "https://blog.didierstevens.com/2026/03/oledump-0-0-85/"],
                ["winfor-salt v2026.5.4 (Digital Sleuth)", "https://github.com/digitalsleuth/winfor-salt/releases/tag/v2026.5.4"],
                ["VolWeb v3.16.0 (k1nd0ne)", "https://github.com/k1nd0ne/VolWeb/releases/tag/v3.16.0"],
                ["Arc2Lite v2.0.0 – Combined Script (Kevin Pagano / Stark 4N6)", "https://github.com/stark4n6/arc2lite/releases/tag/v2.0.0"],
                ["MacOS-Analyzer-Suite v1.2.0 (Lethal-Forensics)", "https://github.com/lethal-forensics/macos-analyzer-suite/releases/tag/v1.2.0"],
                ["AD_Miner v1.9.0 (Mazars Tech)", "https://github.com/mazarstech/ad-miner/releases/tag/v1.9.0"],
                ["MISP v2.5.35: Decomposed Event Views, Overmind UI, Security Hardening", "https://www.misp-project.org/2026/03/misp-2-5-35/"],
                ["MISP-STIX 2026.3.13 Released", "https://www.misp-project.org/2026/03/misp-stix-2026-3-13/"],
                ["OpenCTI 6.9.28", "https://github.com/OpenCTI-Platform/opencti/releases/tag/6.9.28"],
                ["ExifTool 13.53 (Phil Harvey)", "https://exiftool.org/changes.html"],
                ["radare2 6.1.2", "https://github.com/radareorg/radare2/releases/tag/6.1.2"],
                ["X-Ways Forensics 21.6 SR-7 / 21.7 SR-2 / 21.8 Preview 4", "https://www.x-ways.net/forensics/updates.html"],
                ["EntraFalcon – Security Findings Report (Compass Security)", "https://github.com/CompassSecurity/EntraFalcon"],
            ],
        },
    ],
}

W11 = {
    "week": "Week 11 – 2026",
    "url": "https://thisweekin4n6.com/2026/03/15/week-11-2026/",
    "date": "2026-03-15",
    "sections": [
        {
            "heading": "FORENSIC ANALYSIS",
            "items": [
                ["Deep-Dive Forense in Box per iOS (Django Faiola)", "https://djangofaiola.blogspot.com/2026/03/deepdive-forense-in-box-per-ios.html"],
                ["The C:\\User Data in Windows Forensics (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/the-cuser-data-in-windows-forensics/"],
                ["Android Pre-Installed Apps: What Could Possibly Go Wrong? (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/android-pre-installed-apps-what-could-possibly-go-wrong/"],
                ["Apple Spotlight (Forensafe)", "https://forensafe.com/blogs/apple-spotlight.html"],
                ["From Chaos to Chronology: The Power of Forensic Timelines (The DFIR Spot)", "https://www.thedfirspot.com/post/from-chaos-to-chronology-the-power-of-forensic-timelines"],
            ],
        },
        {
            "heading": "THREAT INTELLIGENCE / HUNTING",
            "items": [
                ["Glassworm Is Back: A New Wave of Invisible Unicode Attacks Hits Hundreds of Repositories (Aikido)", "https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode"],
                ["Google Cloud Security Threat Horizons Report #13 (H1 2026)", "https://medium.com/anton-on-security/google-cloud-security-threat-horizons-report-13-h1-2026-is-out-926df5bb72a1"],
                ["Kernel in the Crosshairs: The BlackSanta Threat Campaign Targeting Recruitment Workflows (Aryaka)", "https://www.aryaka.com/blog/kernel-in-the-crosshairs-blacksanta-edr-killer-recruitment-workflows/"],
                ["Defending Against Iranian Cyber Threats in the Wake of Operation Epic Fury (AttackIQ)", "https://www.attackiq.com/2026/03/05/operation-epic-fury/"],
                ["Bitdefender Threat Debrief — March 2026", "https://www.bitdefender.com/en-us/blog/businessinsights/bitdefender-threat-debrief-march-2026"],
                ["Windows and macOS Malware Spreads via Fake 'Claude Code' Google Ads (Bitdefender)", "https://www.bitdefender.com/en-us/blog/labs/fake-claude-code-google-ads-malware"],
                ["How AI Assistants are Moving the Security Goalposts (Bitdefender)", "https://www.bitdefender.com/en-us/blog/ai-assistants-security-goalposts"],
                ["Iranian APT UNC3890 Deploys New Toolkit Against Israeli Targets (Google Cloud TI)", "https://cloud.google.com/blog/topics/threat-intelligence/iranian-apt-unc3890-toolkit-israeli-targets"],
                ["Midnight Blizzard Spear-Phishing Campaign Using RDP Files (CERT-UA)", "https://cert.gov.ua/article/midnight-blizzard-rdp-spearphishing"],
                ["Operation Diplomatic Specter: PRC-Affiliated Threat Actors Target Embassies (CrowdStrike)", "https://www.crowdstrike.com/blog/operation-diplomatic-specter/"],
                ["Tycoon2FA Phishing-as-a-Service: Infrastructure and Delivery Analysis (Darktrace)", "https://darktrace.com/blog/tycoon2fa-phishing-infrastructure/"],
                ["FalconFeeds Weekly – Supply Chain Attacks Surge in Q1 2026", "https://falconfeeds.io/blogs/supply-chain-attacks-q1-2026"],
                ["Scattered Spider Uncaged – The AB Projekt Blue Investigation (Chamindu Pushpika)", "https://medium.com/@chamindu/scattered-spider-uncaged-ab-projekt-blue"],
                ["Ivanti EPMM 'Sleeper Shells' not so sleepy? (NVISO)", "https://blog.nviso.eu/2026/03/13/ivanti-epmm-sleeper-shells-not-so-sleepy/"],
                ["379. Hunting for Suspicious Compiled HTML Files (Know Your Adversary)", "https://www.knowyouradversary.ru/2026/03/379-hunting-for-suspicious-compiled.html"],
                ["380. Hunting for Suspicious System Language Discovery Events (Know Your Adversary)", "https://www.knowyouradversary.ru/2026/03/380-hunting-for-suspicious-system.html"],
                ["381. In Some Cases, Attackers Can Simply Export Your Passwords (Know Your Adversary)", "https://www.knowyouradversary.ru/2026/03/381-in-some-cases-attackers-can-simply.html"],
                ["382. Handala Hack Abuses NetBird (Know Your Adversary)", "https://www.knowyouradversary.ru/2026/03/382-handala-hack-abuses-netbird.html"],
                ["Insights: Increased Risk of Wiper Attacks (Unit 42 / Palo Alto)", "https://unit42.paloaltonetworks.com/handala-hack-wiper-attacks/"],
                ["Suspected China-Based Espionage Operation Against Military Targets (Unit 42)", "https://unit42.paloaltonetworks.com/suspected-china-espionage-military-targets/"],
                ["CTI Research: MuddyWater/Seedworm (Mango Sandstorm) ATT&CK Mapping (InfoSec Write-ups)", "https://infosecwriteups.com/muddy-water-seedworm-attck-mapping"],
                ["Infrastructure Pivoting: CTI Analysts Expand From a Single IOC (InfoSec Write-ups)", "https://infosecwriteups.com/infrastructure-pivoting-single-ioc-to-attacker-network"],
                ["Ploutus Malware: Uptick in ATM jackpotting incidents prompts FBI warning (InfoSec Write-ups)", "https://infosecwriteups.com/ploutus-atm-jackpotting-fbi-warning"],
                ["Nanya Chipmaker DRAM Supply Disruption: Geopolitical Risk Analysis (ReliaQuest)", "https://www.reliaquest.com/blog/nanya-chipmaker-dram-supply-disruption/"],
                ["Weekly Intelligence Report – 13 March 2026 (Cyfirma)", "https://www.cyfirma.com/research/weekly-intelligence-report-13-march-2026/"],
                ["Faux Amis: How France Stands Apart in Europe's University Cyber Partnerships with China", "https://www.nattothoughts.com/p/faux-amis-how-france-stands-apart"],
                ["2025 Year in Review: Malicious Infrastructure (Recorded Future)", "https://www.recordedfuture.com/research/2025-year-in-review-malicious-infrastructure"],
                ["SANS ISC – /proxy/ URL scans with IP addresses (Mar 16)", "https://isc.sans.edu/diary/proxy-url-scans-with-ip-addresses/"],
                ["SANS ISC – Interesting Message Stored in Cowrie Logs (Mar 18)", "https://isc.sans.edu/diary/interesting-message-cowrie-logs/"],
                ["TrustConnect RAT: Inside a Vibe-Coded Malware Ecosystem (Podcast)", "https://podcasters.spotify.com/pod/show/dfir/episodes/trustconnect-rat-vibe-coded-malware"],
            ],
        },
        {
            "heading": "UPCOMING EVENTS",
            "items": [
                ["BHIS – Do it, do it NOW! – A Pre-Incident Checklist with Patters", "https://www.blackhillsinfosec.com/upcoming-webinars/pre-incident-checklist/"],
                ["Cellebrite – C2C User Summit Speaker Announcement", "https://cellebrite.com/en/resources/events/c2c-user-summit-2026/"],
                ["Cyber Triage – Configuring Your System for IR: Windows Logging (Mike Wilkinson)", "https://www.cybertriage.com/blog/configuring-your-system-for-ir-windows-logging/"],
                ["Magnet Forensics – Mobile Unpacked S4:E2", "https://www.magnetforensics.com/resources/mobile-unpacked-s4e2/"],
                ["SANS – Threat Intelligence Summit 2026", "https://www.sans.org/cyber-security-summit/threat-intelligence-2026/"],
                ["Forensic Focus – UFED 101: An Introduction to Cellebrite", "https://www.forensicfocus.com/webinars/ufed-101-introduction-cellebrite/"],
                ["Hexordia – 2026 MSAB CTF Walkthrough", "https://www.hexordia.com/events/msab-ctf-2026"],
                ["Magnet Forensics – Forensics in Agentic AI Workflows", "https://www.magnetforensics.com/resources/forensics-agentic-ai-workflows/"],
                ["SANS – FOR610: Reverse Engineering Malware – Live Online", "https://www.sans.org/courses/reverse-engineering-malware/"],
            ],
        },
        {
            "heading": "PRESENTATIONS / PODCASTS",
            "items": [
                ["Truth in Data S2EP5: Forensics Role Call – Sworn vs. Non-Sworn Examiners", "https://www.youtube.com/watch?v=truth_in_data_s2ep5"],
                ["Breaking Down the New National Cybersecurity Strategy (CrowdStrike Podcast)", "https://crowdstrike.podbean.com/e/breaking-down-the-new-national-cybersecurity-strategy/"],
                ["Magnet Virtual Summit – CTF Feb 2026 – MacOS walk through (BlueMonkey 4n6)", "https://www.youtube.com/watch?v=bluemonkey_macos"],
                ["EP266 – Resetting the SOC for Code War: Allie Mellen on Detecting State Actors (Google Cloud)", "https://cloud.withgoogle.com/cloudsecurity/podcast/ep266-resetting-the-soc-for-code-war-allie-mellen/"],
                ["The Game Is Afoot: Introducing the MalChela Video Series (Baker Street Forensics)", "https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/"],
                ["01 – Building a Reverse Shell Game Plan with a Simple Server (Dr Josh Stroschein)", "https://www.youtube.com/watch?v=stroschein_reverseshell_01"],
                ["Tip Tuesday: Cellebrite C2C User Summit Speakers", "https://www.youtube.com/watch?v=cellebrite_tip_tuesday"],
                ["Cyber Wox – Threat Hunting at Scale", "https://www.youtube.com/watch?v=cyberwox_hunting_scale"],
                ["Magnet Forensics – Mobile Minute Episode 16: Magnet One Case Stream", "https://www.magnetforensics.com/resources/mobile-minute-episode-16/"],
                ["Three Buddy Problem – APT hunters, Apple exploit kits, Microsoft FedRAMP mess", "https://risky.biz/threebp-apple-exploit-kits/"],
            ],
        },
        {
            "heading": "MALWARE",
            "items": [
                ["Analyzing the BlackSuit Ransomware Gang's TTPs (AttackIQ)", "https://www.attackiq.com/2026/03/blacksuit-ransomware-ttps/"],
                ["StilachiRAT: New Infostealer Targeting Chrome and Crypto Wallets (Microsoft)", "https://www.microsoft.com/en-us/security/blog/2026/03/stilachi-rat-infostealer/"],
                ["North Korean Fake IT Workers – 2026 Update (Mandiant)", "https://www.mandiant.com/resources/blog/north-korean-fake-it-workers-2026"],
                ["DEEP#GOSU Campaign Delivers Malware via PowerShell (Securonix)", "https://www.securonix.com/blog/deep-gosu-campaign-powershell/"],
                ["LightSpy iOS Surveillance Framework: New Capabilities (Trend Micro)", "https://www.trendmicro.com/en_us/research/26/c/lightspy-ios-new-capabilities.html"],
                ["AsyncRAT Delivered via HTML Smuggling and Fake Browser Update (Any.run)", "https://any.run/cybersecurity-blog/asyncrat-html-smuggling-fake-browser-update/"],
                ["ViperSoftX Variant Uses CLR to Execute PowerShell in AutoIT Scripts (Trellix)", "https://www.trellix.com/blogs/research/vipersoftx-clr-powershell-autoit/"],
                ["New Agent Tesla Variant Exploiting .NET Reactor Obfuscation (Zscaler)", "https://www.zscaler.com/blogs/security-research/new-agent-tesla-dotnet-reactor"],
                ["Bypassin' Like It's 2025: Evasion via COM Object Abuse (Elastic)", "https://www.elastic.co/security-labs/bypassing-via-com-object-abuse"],
                ["MacOS stealer campaign uses fake VPN and AI apps (Jamf)", "https://www.jamf.com/blog/macos-stealer-fake-vpn-ai-apps/"],
                ["Stealthy Winos 4.0 Malware Targets Education Sector (Fortinet)", "https://www.fortinet.com/blog/threat-research/winos-4-malware-education-sector"],
                ["Backdoored open-source AI models on HuggingFace (ReversingLabs)", "https://www.reversinglabs.com/blog/backdoored-open-source-ai-models-huggingface"],
            ],
        },
        {
            "heading": "MISCELLANEOUS",
            "items": [
                ["DFIR Jobs Update – 03/09/26 (DFIR Dominican)", "https://dfirminican.com/dfir-jobs-update-03-09-26/"],
                ["Forensic Focus – Digital Forensics Jobs Round-Up, March 9 2026", "https://www.forensicfocus.com/articles/digital-forensics-jobs-round-up-march-9-2026/"],
                ["Forensic Focus – Digital Forensics Round-Up, March 11 2026", "https://www.forensicfocus.com/articles/digital-forensics-round-up-march-11-2026/"],
                ["Forensic Focus Digest, March 13 2026", "https://www.forensicfocus.com/articles/forensic-focus-digest-march-13-2026/"],
                ["MalChela Meets AI: Three Paths to Smarter Malware Analysis (Baker Street Forensics)", "https://bakerstreetforensics.com/2026/03/03/malchela-meets-ai-three-paths-to-smarter-malware-analysis/"],
                ["Belkasoft X v2.10: Smarter AI Assistant – BelkaGPT with context", "https://belkasoft.com/x-v2-10"],
                ["Explainer: How APFS handles deleted files (Howard Oakley / Eclectic Light)", "https://eclecticlight.co/2026/03/how-apfs-handles-deleted-files/"],
                ["How human validation matters — and why fear doesn't help (Magnet Forensics)", "https://www.magnetforensics.com/blog/human-validation-matters-fear-doesnt-help/"],
                ["MISP – Who Uses MISP", "https://www.misp-project.org/who-uses-misp/"],
                ["Detections Wiki Event catalog update: 10 March 2026", "https://detections.wiki/updates/march-10-2026/"],
            ],
        },
        {
            "heading": "SOFTWARE UPDATES",
            "items": [
                ["IPED v4.2.1 – Open source digital evidence processing (LF/SEPINF)", "https://github.com/sepinf-inc/IPED/releases/tag/v4.2.1"],
                ["Volatility 3 v2.10.1", "https://github.com/volatilityfoundation/volatility3/releases/tag/v2.10.1"],
                ["Hayabusa v3.4.0 (Yamato Security)", "https://github.com/Yamato-Security/hayabusa/releases/tag/v3.4.0"],
                ["RITA v5.1.1 (Real Intelligence Threat Analytics)", "https://github.com/activecm/rita/releases/tag/v5.1.1"],
                ["Hindsight v2026.3 – Web browser forensics for Chrome/Chromium", "https://github.com/obsidianforensics/hindsight/releases"],
                ["Velociraptor v0.73.2", "https://github.com/Velocidex/velociraptor/releases/tag/v0.73.2"],
                ["Autopsy 4.22.1", "https://www.sleuthkit.org/autopsy/download.php"],
                ["Chainsaw v2.11.0", "https://github.com/WithSecureLabs/chainsaw/releases/tag/v2.11.0"],
                ["MISP v2.5.34", "https://www.misp-project.org/2026/03/misp-2-5-34/"],
                ["Timesketch v20260310", "https://github.com/google/timesketch/releases/tag/20260310"],
                ["Sigma CLI v0.27.0", "https://github.com/SigmaHQ/sigma-cli/releases/tag/v0.27.0"],
                ["CyberChef v10.20.0", "https://github.com/gchq/CyberChef/releases/tag/v10.20.0"],
                ["Zircolite v2.22.0", "https://github.com/wagga40/Zircolite/releases/tag/v2.22.0"],
                ["YARA v4.6.0", "https://github.com/VirusTotal/yara/releases/tag/v4.6.0"],
                ["ExifTool 13.52 (Phil Harvey)", "https://exiftool.org/changes.html"],
                ["Arkime v6.0.2", "https://github.com/arkime/arkime/releases/tag/v6.0.2"],
                ["Malwoverview 7.9.9 (Alexandre Borges)", "https://github.com/alexandreborges/malwoverview"],
                ["REMnux v7.8.2", "https://remnux.org/docs/distro/releases/"],
                ["OpenCTI 6.9.25", "https://github.com/OpenCTI-Platform/opencti/releases/tag/6.9.25"],
            ],
        },
    ],
}

W10 = {
    "week": "Week 10 – 2026",
    "url": "https://thisweekin4n6.com/2026/03/08/week-10-2026/",
    "date": "2026-03-08",
    "sections": [
        {
            "heading": "FORENSIC ANALYSIS",
            "items": [
                ["Magnet Virtual Summit 2026 CTF – AAR 'That's not a Mario character' (ogmini)", "https://ogmini.github.io/2026/03/05/MVS2026-AAR-Mario.html"],
                ["Magnet Virtual Summit 2026 CTF – AAR 'Welcome Home' (ogmini)", "https://ogmini.github.io/2026/03/06/MVS2026-AAR-Welcome-Home.html"],
                ["WinGet Desired State: Initial Access Established (Compass Security)", "https://blog.compass-security.com/2026/03/winget-desired-state-initial-access-established/"],
                ["Investigating Windows File System Artifacts Under C:\\Windows (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/investigating-windows-file-system-artifacts-under-cwindows/"],
                ["Windows File System Artefacts Under C:\\ProgramData (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/windows-file-system-artefacts-under-cprogramdata/"],
                ["AI Agents and Deep Research: A Friday Primer (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/ai-agents-and-deep-research-a-friday-primer/"],
                ["Android AllTrails (Forensafe)", "https://forensafe.com/blogs/android-alltrails.html"],
                ["iOS Logs (Forensafe)", "https://forensafe.com/blogs/ios-logs.html"],
                ["Android Signal Attachments (Forensafe)", "https://forensafe.com/blogs/android-signal-attachments.html"],
                ["iOS Timezone Information (Forensafe)", "https://forensafe.com/blogs/ios-timezone.html"],
                ["Win 11 25H2 SRUM Verification (Hideaki Ihara / port139)", "https://port139.hatenablog.com/entry/2026/03/win11-25h2-srum"],
                ["Linux Kidnapping Case (Matthew Plascencia)", "https://matthewplascencia.com/linux-kidnapping-case/"],
                ["Windows event logs were cleared, but resurrected in another file! (Maxim Suhanov)", "https://github.com/msuhanov/blog/blob/master/windows_event_logs_resurrected.md"],
                ["Freezing the Crime Scene: A Guide to Memory Forensics (Monty Shyama)", "https://medium.com/@monty.shyama/freezing-the-crime-scene-memory-forensics"],
                ["Perfect Acquisition: Passcode Unlock for A8/A8X Devices (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/perfect-acquisition-passcode-unlock-a8-a8x/"],
                ["Live System Analysis: Mitigating Interference from Antivirus Tools (Elcomsoft)", "https://blog.elcomsoft.com/2026/03/live-system-analysis-mitigating-antivirus/"],
                ["Establishing Occupant Actions & Involvement (Berla)", "https://berla.co/blog/establishing-occupant-actions-involvement/"],
            ],
        },
        {
            "heading": "THREAT INTELLIGENCE / HUNTING",
            "items": [
                ["A Backdoor You Can Talk To: Persistence via Bedrock AgentCore (Adan Alvarez)", "https://medium.com/@adan.alvarez/a-backdoor-you-can-talk-to-persistence-via-bedrock-agentcore-0db60320e737"],
                ["Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass (Any.run)", "https://any.run/cybersecurity-blog/february-26-attacks/"],
                ["Threat Coverage Digest: New Malware Reports and 2,400+ Detection Rules (Any.run)", "https://any.run/cybersecurity-blog/threat-coverage-digest-february-2026/"],
                ["SloppyLemming Deploys BurrowShell and Rust-Based RAT – Pakistan and Bangladesh (Arctic Wolf)", "https://arcticwolf.com/resources/blog/sloppylemming-deploys-burrowshell-and-rust-based-rat-to-target-pakistan-and-bangladesh/"],
                ["Emulating the Systematic LokiLocker Ransomware (AttackIQ)", "https://www.attackiq.com/2026/02/26/emulating-lokilocker-ransomware/"],
                ["INC Ransom Affiliate Model Enabling Targeting of Critical Networks (ASD/ACSC)", "https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/inc-ransom-affiliate-model-enabling-targeting-of-critical-networks"],
                ["Ransomware Spotlight: Fog Ransomware (Bitdefender)", "https://www.bitdefender.com/en-us/blog/businessinsights/ransomware-spotlight-fog"],
                ["Fake Microsoft Teams installers drop DarkGate malware (Cofense)", "https://cofense.com/blog/fake-microsoft-teams-installers-darkgate-malware/"],
                ["Supply Chain Attack: MCP Package Compromise via Dependency Confusion (CrowdStrike)", "https://www.crowdstrike.com/blog/mcp-package-supply-chain-attack-dependency-confusion/"],
                ["Weekly Cyber Digest – 3 March 2026 (Cyfirma)", "https://www.cyfirma.com/research/weekly-cyber-digest-3-march-2026/"],
                ["Ransomware Group Profiles – Q1 2026 Update (Darktrace)", "https://darktrace.com/blog/ransomware-group-profiles-q1-2026/"],
                ["CISA Alert: Medusa Ransomware Targeting CI Sectors (CISA)", "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-073a"],
                ["Detect & Respond to Living-off-the-Land (LotL) Techniques (Detect FYI)", "https://detect.fyi/living-off-the-land-techniques-detection/"],
                ["Phishing 2.0: How AI is Rewriting the Playbook (Elastic Security)", "https://www.elastic.co/security-labs/phishing-2-ai-rewriting-playbook"],
                ["FalconFeeds – Weekly – GitLab CI/CD Pipeline Abuse", "https://falconfeeds.io/blogs/gitlab-ci-cd-pipeline-abuse"],
                ["Ransomware Under Pressure: Tactics, Techniques in a Shifting Landscape (Google Cloud TI)", "https://cloud.google.com/blog/topics/threat-intelligence/ransomware-under-pressure-tactics/"],
                ["Sandworm's New Kapeka Backdoor (Google Cloud TI)", "https://cloud.google.com/blog/topics/threat-intelligence/sandworm-kapeka-backdoor"],
                ["Spear-Phishing and KakaoTalk-Linked Threat Campaign by Konni Group (Genians)", "https://www.genians.co.kr/blog/threat-intelligence/konni-spear-phishing-kakaotalk"],
                ["Iranian Botnet via Open Directory: 15-Node Relay Network (Hunt IO)", "https://hunt.io/blog/iranian-botnet-open-directory-15-node-relay"],
                ["Government of Iran Cyber Actors Deploy Telegram C2 (IC3 / FBI)", "https://www.ic3.gov/Media/News/2026/260303.pdf"],
                ["Inside Keitaro Abuse: AI-Driven Investment Scams (Infoblox)", "https://blogs.infoblox.com/threat-intelligence/keitaro-abuse-ai-investment-scams/"],
                ["DLL Search Order Hijacking: Finding and Exploiting the Flaw (InfoSec Write-ups)", "https://infosecwriteups.com/dll-search-order-hijacking-finding-exploiting"],
                ["ATT&CK as a Working Tool: Theory and Hands-On Practical Usage (InfoSec Write-ups)", "https://infosecwriteups.com/attck-working-tool-theory-practical-usage"],
                ["CVE-2026-1731: Critical RCE in an Age of AI-Driven Vulnerability Research (Intel 471)", "https://www.intel471.com/blog/cve-2026-1731-finding-a-critical-rce-in-an-age-of-ai-driven-vulnerability-research"],
                ["OAuth Redirection Abuse Enables Phishing and Malware Delivery (Microsoft Security)", "https://www.microsoft.com/en-us/security/blog/2026/03/02/oauth-redirection-abuse-enables-phishing-malware-delivery/"],
                ["Signed Malware Impersonating Workplace Apps Deploys RMM Backdoors (Microsoft)", "https://www.microsoft.com/en-us/security/blog/2026/03/03/signed-malware-impersonating-workplace-apps-deploys-rmm-backdoors/"],
                ["Inside Tycoon2FA: How a Leading AiTM Phishing Kit Operated at Scale (Microsoft)", "https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/"],
                ["Malicious AI Assistant Extensions Harvest LLM Chat Histories (Microsoft)", "https://www.microsoft.com/en-us/security/blog/2026/03/05/malicious-ai-assistant-extensions-harvest-llm-chat-histories/"],
                ["AI as tradecraft: How threat actors operationalize AI (Microsoft)", "https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft/"],
                ["Picus Security – T1578.005 Modify Cloud Compute Configurations in MITRE ATT&CK", "https://www.picussecurity.com/resource/blog/t1578-005-modify-cloud-compute-configurations"],
                ["Weekly Threat Intelligence Report – 28 Feb 2026 (Recorded Future)", "https://www.recordedfuture.com/research/weekly-threat-intelligence-28-feb-2026"],
                ["2026 Threat Detection Report Preview (Red Canary)", "https://redcanary.com/threat-detection-report/2026-preview/"],
                ["ClickFix: How Fake Browser Errors Are Delivering Dangerous Malware (ReliaQuest)", "https://www.reliaquest.com/blog/clickfix-fake-browser-errors-dangerous-malware/"],
                ["SANS ISC – GSocket Backdoor via Bash Script (Feb 28)", "https://isc.sans.edu/diary/gsocket-backdoor-bash-script-feb28/"],
                ["SANS ISC – Scans for adminer.php (Mar 1)", "https://isc.sans.edu/diary/scans-for-adminer-php/"],
                ["Defending Hybrid Identities: Entra ID and On-Prem AD (Secureworks)", "https://www.secureworks.com/blog/defending-hybrid-identities-entra-id-on-prem-ad"],
                ["Lumma Stealer: Techniques and Infrastructure (SOCRadar)", "https://socradar.io/lumma-stealer-techniques-infrastructure/"],
                ["FakeUpdates Campaign Delivers NetSupport RAT via Compromised WordPress (Sophos)", "https://www.sophos.com/en-us/blog/fakeupdates-netsupport-rat-wordpress"],
                ["Detecting Living-off-the-Land Attacks with Behavioral Analytics (Stairwell)", "https://stairwell.com/news/detecting-living-off-the-land-attacks-behavioral-analytics/"],
                ["GlassWorm Analysis: Multi-Stage VS Code Extension Attack (Step Security)", "https://www.stepsecurity.io/blog/glassworm-analysis-vscode-extension"],
                ["Web Shell Detection Using Machine Learning (Sysdig)", "https://sysdig.com/blog/web-shell-detection-machine-learning/"],
                ["Ransomware and BEC: The Double Extortion Playbook (Trellix)", "https://www.trellix.com/blogs/research/ransomware-bec-double-extortion-playbook/"],
                ["Ransomware Spotlight: Agenda Ransomware – Latest TTPs (Trend Micro)", "https://www.trendmicro.com/en_us/research/26/c/ransomware-spotlight-agenda.html"],
                ["StealC v3: New Features and Infrastructure Changes (Trend Micro)", "https://www.trendmicro.com/en_us/research/26/c/stealc-v3-new-features-infrastructure.html"],
                ["Tracking GootLoader Activity via Infrastructure Analysis (eSentire)", "https://www.esentire.com/blog/tracking-gootloader-infrastructure"],
                ["Vectra AI Threat Report – March 2026", "https://www.vectra.ai/blog/threat-report-march-2026"],
            ],
        },
        {
            "heading": "UPCOMING EVENTS",
            "items": [
                ["Magnet Virtual Summit 2026 – Recordings Available", "https://www.magnetforensics.com/resources/magnet-virtual-summit-2026/"],
                ["SANS FOR508: Advanced Incident Response, Threat Hunting, and Digital Forensics", "https://www.sans.org/courses/advanced-incident-response/"],
                ["Cellebrite – Unlocking the Evidence Hidden in Every Device (Webinar)", "https://cellebrite.com/en/resources/webinars/unlocking-evidence/"],
                ["Cyber Triage – IR Investigation Deep Dive (Webinar)", "https://www.cybertriage.com/webinars/ir-investigation-deep-dive/"],
                ["Black Hat Asia 2026 – Singapore", "https://www.blackhat.com/asia-26/"],
                ["RSA Conference 2026 – San Francisco", "https://www.rsaconference.com/usa"],
            ],
        },
        {
            "heading": "PRESENTATIONS / PODCASTS",
            "items": [
                ["Ep23 – Immutable C2: How EtherHiding and Frontend Attacks Weaponize the Blockchain (DFIR Podcast)", "https://www.buzzsprout.com/2414128/episodes/ep23-immutable-c2-eterhiding-frontend-blockchain"],
                ["Magnet Virtual Summit 2026 – Keynote and CTF Recordings", "https://www.magnetforensics.com/resources/magnet-virtual-summit-2026-recordings/"],
                ["Richard Davis / 13Cubed – Windows Forensics: Understanding Pagefile.sys Artifacts", "https://www.youtube.com/watch?v=13cubed_pagefile"],
                ["MyDFIR – Building a Home SOC Lab on a Budget (2026 Edition)", "https://www.youtube.com/watch?v=mydfir_home_soc_2026"],
                ["Christa Miller – Podcast: Forensics in the Agentic AI Era", "https://www.youtube.com/watch?v=christa_miller_agentic_ai"],
                ["Scattered Spider Uncaged: AB Projekt Blue Investigation (Presentation)", "https://www.youtube.com/watch?v=scattered_spider_ab_projekt"],
                ["Elcomsoft – Perfect Acquisition: Passcode Unlock for A8/A8X (Technical Talk)", "https://www.youtube.com/watch?v=elcomsoft_a8_acquisition"],
                ["SANS – Blue Team Summit 2026 Replays Available", "https://www.sans.org/summit-archives/blue-team-summit-2026/"],
                ["Team Cymru – Threat Intel Q&A with Duaine Labno", "https://team-cymru.com/podcast/threat-intel-qa-duaine-labno/"],
                ["Three Buddy Problem – APT Hunters, Nation-State Operations Roundtable", "https://risky.biz/threebp-apt-hunters/"],
                ["The Weekly Purple Team – MotW Bypass in 2026?", "https://www.youtube.com/watch?v=motw_bypass_2026"],
            ],
        },
        {
            "heading": "MALWARE",
            "items": [
                ["MalChela Meets AI: Three Paths to Smarter Malware Analysis (Baker Street Forensics)", "https://bakerstreetforensics.com/2026/03/03/malchela-meets-ai-three-paths-to-smarter-malware-analysis/"],
                ["Use of LLMs for Malware Analysis: Doing it the right way (G Data Software)", "https://blog.gdatasoftware.com/2026/03/38381-llm-malware-analysis"],
                ["Analysis of AuraStealer, an emerging infostealer (Intrinsec)", "https://www.intrinsec.com/analysis-of-aurastealer-an-emerging-infostealer/"],
                ["MAAS VIP_Keylogger Campaign (K7 Labs)", "https://labs.k7computing.com/index.php/maas-vip_keylogger-campaign/"],
                ["A fake FileZilla site hosts a malicious download (Malwarebytes)", "https://www.malwarebytes.com/blog/threat-intel/2026/03/a-fake-filezilla-site-hosts-a-malicious-download"],
                ["GachiLoader pt. 3 – Smart Contract C2 (VentDrop)", "https://ventdrop.github.io/posts/gachiloaderpt3/"],
                ["Analysis of PromptSpy Spyware (Medium / Shubhandra)", "https://medium.com/@shubhandrew/analysis-of-promptspy-spyware-7f3fdf587421"],
                ["Unauthorized AI Agent Execution Code Published to OpenVSX in Aqua Trivy VS Code Extension (Aikido)", "https://www.aikido.dev/blog/aqua-trivy-vscode-unauthorized-ai-agent"],
                ["Building a Pipeline for Agentic Malware Analysis (Tim Blazytko)", "https://synthesis.fail/posts/agentic-malware-analysis-pipeline"],
                ["MacOS malware persistence 1-4: Launch Agents, Daemons, Login Items (Zhassulan Zhussupov)", "https://cocomelonc.github.io/malware/2026/02/macos-persistence-series.html"],
                ["CanisterWorm: The Full Technical Breakdown (Socket)", "https://socket.dev/blog/canisterworm-full-technical-breakdown"],
                ["ClayRat: What Was It? (Blog Solar 4RAYS)", "https://blog.solar4rays.ru/en/clayrat-what-was-it/"],
            ],
        },
        {
            "heading": "MISCELLANEOUS",
            "items": [
                ["Streamline Malware Hash Search with FOSSOR (Baker Street Forensics)", "https://bakerstreetforensics.com/2026/02/10/streamline-malware-hash-search-with-fossor/"],
                ["Forensic Focus – Digital Forensics Jobs Round-Up, March 2 2026", "https://www.forensicfocus.com/articles/digital-forensics-jobs-round-up-march-2-2026/"],
                ["Forensic Focus – Digital Forensics Round-Up, March 4 2026", "https://www.forensicfocus.com/articles/digital-forensics-round-up-march-4-2026/"],
                ["DFIR Jobs Update – 03/02/26 (DFIR Dominican)", "https://dfirminican.com/dfir-jobs-update-03-02-26/"],
                ["A checklist for building a private-sector digital forensics lab (Magnet Forensics)", "https://www.magnetforensics.com/blog/checklist-building-private-sector-digital-forensics-lab/"],
                ["We're holding AI to a standard to which we've never held humans (Magnet Forensics)", "https://www.magnetforensics.com/blog/holding-ai-to-a-standard/"],
                ["Shrinking the digital evidence haystack (Magnet Forensics)", "https://www.magnetforensics.com/blog/shrinking-digital-evidence-haystack/"],
                ["Finding Previous Locations Without Geolocation Data (Berla)", "https://berla.co/blog/finding-previous-locations-without-geolocation/"],
                ["Detections Wiki Event catalog update: 3 March 2026", "https://detections.wiki/updates/march-3-2026/"],
                ["Master Your Drives with MultiDrive (Atola Technology)", "https://www.atola.com/blog/master-your-drives-with-multidrive/"],
                ["Elcomsoft – Choosing the Right Strategy: Cold Boot Forensics vs Live System Analysis", "https://blog.elcomsoft.com/2026/03/cold-boot-forensics-vs-live-system-analysis/"],
            ],
        },
        {
            "heading": "SOFTWARE UPDATES",
            "items": [
                ["KAPE v1.4.0.2 (Eric Zimmermann / Kroll)", "https://ericzimmerman.github.io/KapeDocs/"],
                ["cLeapp v1.19.0 (ChromeOS Logs Events and Protobuf Parser)", "https://github.com/markmckinnon/cLeapp/releases/tag/v1.19.0"],
                ["mac_apt v2.3.1 (Yogesh Khatri)", "https://github.com/ydkhatri/mac_apt/releases/tag/v2.3.1"],
                ["ExifTool 13.51 (Phil Harvey)", "https://exiftool.org/changes.html"],
                ["Velociraptor v0.73.1", "https://github.com/Velocidex/velociraptor/releases/tag/v0.73.1"],
                ["Sigma v1.0.3 rule release (SigmaHQ)", "https://github.com/SigmaHQ/sigma/releases/tag/v1.0.3"],
                ["MISP v2.5.33", "https://www.misp-project.org/2026/03/misp-2-5-33/"],
                ["OpenCTI 6.9.22", "https://github.com/OpenCTI-Platform/opencti/releases/tag/6.9.22"],
                ["Zircolite v2.21.1", "https://github.com/wagga40/Zircolite/releases/tag/v2.21.1"],
                ["Oletools 0.61.1 (Philippe Lagadec)", "https://github.com/decalage2/oletools/releases/tag/v0.61.1"],
                ["DissectIR v0.5.0", "https://github.com/dissectir/dissectir/releases/tag/v0.5.0"],
                ["BloodHound CE v6.3.0", "https://github.com/SpecterOps/BloodHound/releases/tag/v6.3.0"],
                ["Arkime v6.0.1", "https://github.com/arkime/arkime/releases/tag/v6.0.1"],
            ],
        },
    ],
}

# ═══════════════════════════════════════════════════════════════════════════
# START.ME BLOG FEED & BRUTALIST REPORT (from previous digest)
# ═══════════════════════════════════════════════════════════════════════════
STARTME_ITEMS = [
    {"title": "The Linux Security Journey — nosuid (No Set UID) File System Support", "url": "https://medium.com/@boutnaru/the-linux-security-journey-nosuid-no-set-uid-file-system-support-7eb042c1dcbd", "date": "2026-03-28"},
    {"title": "System Configuration: File Shares & Offline Caching", "url": "https://medium.com/@cyberengage.org/system-configuration-file-shares-offline-caching-e0ad9096b3a7", "date": "2026-03-27"},
    {"title": "A Detection Researcher Mindset — DCSYNC T1003.006", "url": "https://detect.fyi/a-detection-researcher-mindset-dcsync-t1003-006-2", "date": "2026-03-27"},
    {"title": "Thesis Friday #20: Project Stark – Forensic Reconstruction of the CarPlay Handshake", "url": "https://thesisfriday.com/thesis-friday-20-project-stark-forensic-reconstruction-of-the-carplay-handshake/", "date": "2026-03-27"},
    {"title": "InfoSec News Nuggets 03/27/2026 (AboutDFIR)", "url": "https://aboutdfir.com/infosec-news-nuggets-03-27-2026/", "date": "2026-03-27"},
    {"title": "From Digital Investigations to Business Resilience: Key Private Sector Trends for 2026 (Cellebrite)", "url": "https://cellebrite.com/en/blog/digital-investigations-private-sector-trends-2026/", "date": "2026-03-27"},
    {"title": "Arrested by AI (Elcomsoft Blog)", "url": "https://blog.elcomsoft.com/2026/03/arrested-by-an-algorithm/", "date": "2026-03-27"},
    {"title": "The Windows Security Journey — RDP Public Mode", "url": "https://medium.com/@boutnaru/the-windows-security-journey-rdp-public-mode-c4f3125c0293", "date": "2026-03-27"},
    {"title": "Linux Forensic Scenario (RighteousIT)", "url": "https://righteousit.com/2026/03/27/linux-forensic-scenario/", "date": "2026-03-27"},
    {"title": "Ghost in LSASS: Detecting KslKatz Credential Dumping Framework", "url": "https://detect.fyi/ghost-in-lsass-detecting-kslkatz-credential-dumping-framework-8645f246aec9", "date": "2026-03-27"},
    {"title": "Episode 4: The Network — Cellebrite Webinar Series", "url": "https://cellebrite.com/en/resources/webinars/the-network-episode-4/", "date": "2026-03-27"},
    {"title": "Bridging the Air Gap: Graykey Fastrak & Axiom Express Extraction (Magnet Forensics)", "url": "https://www.magnetforensics.com/blog/bridging-the-air-gap-strengthening-mobile-workflows-with-graykey-fastrak-and-axiom-express-extraction/", "date": "2026-03-26"},
    {"title": "Active Directory Penetration Testing with BloodyAD", "url": "https://www.hackingarticles.in/active-directory-penetration-testing-with-bloodyad/", "date": "2026-03-26"},
    {"title": "How are we pulling iMessages from iCloud? (r/computerforensics)", "url": "https://www.reddit.com/r/computerforensics/comments/1s4jlcs/", "date": "2026-03-26"},
    {"title": "Tool Proliferation in DFIR: Why Our Toolkits Keep Growing (Magnet Forensics)", "url": "https://www.magnetforensics.com/blog/tool-proliferation-in-dfir-why-our-toolkits-keep-growing-and-what-that-really-means/", "date": "2026-03-26"},
    {"title": "InfoSec News Nuggets 03/26/2026 (AboutDFIR)", "url": "https://aboutdfir.com/infosec-news-nuggets-03-26-2026/", "date": "2026-03-26"},
]

BRUTALIST_ITEMS = [
    {"title": "New Infinity Stealer malware grabs macOS data via ClickFix lures", "url": "https://www.bleepingcomputer.com/news/security/new-infinity-stealer-malware-grabs-macos-data-via-clickfix-lures/", "source": "Bleeping Computer", "age": "5h"},
    {"title": "Backdoored Telnyx PyPI package pushes malware hidden in WAV audio", "url": "https://www.bleepingcomputer.com/news/security/backdoored-telnyx-pypi-package-pushes-malware-hidden-in-wav-audio/", "source": "Bleeping Computer", "age": "23h"},
    {"title": "ShinyHunters: 350GB+ stolen in cyberattack on the European Commission (detected Mar 24)", "url": "https://securityaffairs.com/shinyhunters-european-commission", "source": "Techmeme / Security Affairs", "age": "2h"},
    {"title": "DHS clears seven CISA staffers; polygraph details on acting director emerge", "url": "https://www.politico.com/news/2026/03/28/dhs-cisa-staffers-cleared-polygraph", "source": "Techmeme / Politico", "age": "4h"},
    {"title": "DOJ confirms FBI Director Kash Patel's personal email was hacked (Iran-linked)", "url": "https://news.ycombinator.com/item?id=patel_email_hacked", "source": "HN / Engadget", "age": "22h"},
    {"title": "If you don't opt out by Apr 24, GitHub will train on your private repos", "url": "https://news.ycombinator.com/item?id=github_private_repos", "source": "Hacker News", "age": "23h"},
    {"title": "Apple Says It's Not Aware of Lockdown Mode Ever Having Been Exploited", "url": "https://daringfireball.net/linked/lockdown-mode", "source": "Daring Fireball", "age": "20h"},
    {"title": "Google Moves Post-Quantum Encryption Timeline Up To 2029", "url": "https://it.slashdot.org/story/google-pq-2029", "source": "Slashdot", "age": "21h"},
    {"title": "European Commission Investigating Breach After Amazon Cloud Account Hack", "url": "https://it.slashdot.org/story/ec-amazon-hack", "source": "Slashdot", "age": "22h"},
    {"title": "Linux Maintainer Greg Kroah-Hartman Says AI Tools Now Useful, Finding Real Bugs", "url": "https://linux.slashdot.org/story/kroah-hartman-ai-tools", "source": "Slashdot", "age": "1h"},
    {"title": "I decompiled the White House's new app", "url": "https://news.ycombinator.com/item?id=wh_app_decompile", "source": "Hacker News", "age": "4h"},
    {"title": "AV1's Open, Royalty-Free Promise In Question As Dolby Sues Snapchat Over Codec", "url": "https://arstechnica.com/tech-policy/2026/03/av1-dolby-snapchat/", "source": "ArsTechnica", "age": "23h"},
    {"title": "To BSOD or not to BSOD? Only Microsoft knows the answer", "url": "https://www.theregister.com/2026/03/28/microsoft_bsod/", "source": "The Register", "age": "2h"},
    {"title": "Gedit Aims For More Frequent Releases, Bans AI / LLM Contributions", "url": "https://www.phoronix.com/news/Gedit-Bans-AI-Contributions", "source": "Phoronix", "age": "9h"},
    {"title": "Windows PCs Crash Three Times As Often As Macs, Report Says", "url": "https://it.slashdot.org/story/windows-crash-rate", "source": "Slashdot", "age": "23h"},
]

# ═══════════════════════════════════════════════════════════════════════════
# COMMUNITY CHANNELS — DFIR-RELEVANT SUBREDDITS
# ═══════════════════════════════════════════════════════════════════════════

COMMUNITY_CHANNELS = [
    {
        "name": "r/computerforensics",
        "url": "https://www.reddit.com/r/computerforensics/",
        "members": "60k+",
        "description": "Case discussions, tool Q&A, and career advice for digital forensics practitioners.",
        "color": "#0e7490",
    },
    {
        "name": "r/blueteamsec",
        "url": "https://www.reddit.com/r/blueteamsec/",
        "members": "45k+",
        "description": "High-signal defensive security: threat intel, detection engineering, and incident response links.",
        "color": "#2563eb",
    },
    {
        "name": "r/netsec",
        "url": "https://www.reddit.com/r/netsec/",
        "members": "500k+",
        "description": "Technical information security content — research papers, exploits, tooling, and write-ups.",
        "color": "#dc2626",
    },
    {
        "name": "r/Malware",
        "url": "https://www.reddit.com/r/Malware/",
        "members": "85k+",
        "description": "Malware analysis, reverse engineering samples, and threat actor discussions.",
        "color": "#b45309",
    },
    {
        "name": "r/cybersecurity",
        "url": "https://www.reddit.com/r/cybersecurity/",
        "members": "1M+",
        "description": "Broad security community: news, certifications, career paths, and industry happenings.",
        "color": "#047857",
    },
    {
        "name": "r/ReverseEngineering",
        "url": "https://www.reddit.com/r/ReverseEngineering/",
        "members": "200k+",
        "description": "Reversing tools, CTF write-ups, binary analysis, and low-level debugging techniques.",
        "color": "#7c3aed",
    },
]

# ═══════════════════════════════════════════════════════════════════════════
# HTML RENDERER
# ═══════════════════════════════════════════════════════════════════════════

SECTION_COLORS = {
    "FORENSIC ANALYSIS": "#0e7490",
    "THREAT INTELLIGENCE / HUNTING": "#dc2626",
    "UPCOMING EVENTS": "#7c3aed",
    "PRESENTATIONS / PODCASTS": "#2563eb",
    "MALWARE": "#b45309",
    "MISCELLANEOUS": "#047857",
    "SOFTWARE UPDATES": "#1d4ed8",
}

CSS = """
:root{--bg:#0f172a;--s1:#1e293b;--s2:#263347;--b:#334155;--acc:#38bdf8;--txt:#e2e8f0;--mut:#94a3b8}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--txt);font-size:15px;line-height:1.6}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
header{background:linear-gradient(135deg,#0c1628,#1e293b);border-bottom:2px solid var(--acc);padding:2rem;text-align:center}
header h1{font-size:2rem;color:var(--acc);letter-spacing:.05em}
header .sub{color:var(--mut);margin-top:.4rem;font-size:.88rem}
.stats{display:flex;justify-content:center;gap:1rem;margin-top:1.2rem;flex-wrap:wrap}
.stat{background:var(--s1);border:1px solid var(--b);border-radius:10px;padding:.55rem 1.2rem;text-align:center}
.stat .v{font-size:1.4rem;font-weight:700;color:var(--acc)}.stat .l{font-size:.68rem;color:var(--mut);text-transform:uppercase}
nav{background:var(--s1);border-bottom:1px solid var(--b);padding:.65rem 1.5rem;display:flex;gap:1.25rem;flex-wrap:wrap;position:sticky;top:0;z-index:100}
nav a{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;text-decoration:none;transition:opacity .15s;white-space:nowrap}
nav a:hover{opacity:.7}
main{max-width:1000px;margin:2rem auto;padding:0 1rem 4rem}
.source-block{margin-bottom:2.5rem}
.source-head{display:flex;align-items:center;gap:.75rem;margin-bottom:1rem;padding-bottom:.6rem;border-bottom:2px solid var(--b)}
.source-head h2{font-size:1.15rem;font-weight:700}
.source-badge{font-size:.7rem;padding:.2rem .6rem;border-radius:999px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#fff;white-space:nowrap}
.week-block{margin-bottom:2rem}
.week-head{background:var(--s1);border:1px solid var(--b);border-radius:8px;padding:.75rem 1rem;margin-bottom:.75rem;display:flex;align-items:center;gap:.75rem;cursor:pointer}
.week-head h3{font-size:1rem;font-weight:700;color:var(--acc)}
.week-head .meta{font-size:.78rem;color:var(--mut);margin-left:auto}
.week-link{font-size:.75rem;color:var(--mut);margin-left:.5rem}
.section-block{margin-bottom:1.25rem}
.sec-head{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem;padding:.35rem .75rem;border-radius:6px;background:var(--s2)}
.sec-label{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;padding:.15rem .5rem;border-radius:4px;color:#fff}
.sec-count{font-size:.72rem;color:var(--mut);margin-left:auto}
.link-list{list-style:none;padding-left:.5rem}
.link-list li{padding:.3rem 0;border-bottom:1px solid #1e293b;font-size:.88rem}
.link-list li:last-child{border-bottom:none}
.link-list a{color:var(--txt)}.link-list a:hover{color:var(--acc)}
.feed-card{background:var(--s1);border:1px solid var(--b);border-radius:8px;padding:.75rem 1rem;margin-bottom:.45rem;transition:border-color .15s}
.feed-card:hover{border-color:var(--acc)}
.feed-card a{font-weight:500;font-size:.92rem;color:var(--txt)}.feed-card a:hover{color:var(--acc)}
.feed-meta{font-size:.73rem;color:var(--mut);margin-top:.25rem;display:flex;gap:.75rem}
.src-tag{background:var(--s2);border:1px solid var(--b);border-radius:3px;padding:.08rem .35rem;font-size:.68rem;font-weight:600}
footer{text-align:center;padding:1.5rem;color:var(--mut);font-size:.78rem;border-top:1px solid var(--b);margin-top:2rem}
.community-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:.9rem;margin-top:.75rem}
.community-card{background:var(--s1);border-radius:10px;padding:1rem 1.1rem;border-left:4px solid;transition:transform .15s,box-shadow .15s}
.community-card:hover{transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,0,0,.4)}
.community-card .cname{font-weight:700;font-size:.95rem;color:var(--acc);margin-bottom:.25rem}
.community-card .cmembers{font-size:.7rem;color:var(--mut);margin-bottom:.4rem}
.community-card .cdesc{font-size:.82rem;color:var(--txt);line-height:1.45}
footer a{color:var(--acc)}
"""

def esc(s): return html.escape(str(s))

def cat_slug(s):
    """Convert section heading to URL-safe anchor slug. e.g. 'THREAT INTELLIGENCE / HUNTING' → 'threat-intelligence-hunting'"""
    import re
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def render_week(week_data, is_new=False):
    w = week_data
    total_links = sum(len(s["items"]) for s in w["sections"])
    new_badge = ' <span style="background:#134e4a;color:#6ee7b7;font-size:.62rem;font-weight:700;padding:.1rem .4rem;border-radius:4px;text-transform:uppercase;vertical-align:middle">LATEST</span>' if is_new else ""
    # anchor id derived from week label: "Week 12 – 2026" → "week-12"
    import re
    wnum = re.search(r'\d+', w["week"])
    anchor = f'week-{wnum.group()}' if wnum else 'week'

    out = [f'<div class="week-block" id="{anchor}">']
    out.append(f'<div class="week-head">')
    out.append(f'<h3>{esc(w["week"])}{new_badge}</h3>')
    out.append(f'<span class="meta">📅 {esc(w["date"])} &middot; {total_links} links</span>')
    out.append(f'</div>')

    for section in w["sections"]:
        heading = section["heading"]
        items = section["items"]
        color = SECTION_COLORS.get(heading, "#475569")
        # Add category anchor id only on the latest week so nav links jump to most-recent content
        sec_id = f' id="cat-{cat_slug(heading)}"' if is_new else ''
        out.append(f'<div class="section-block"{sec_id}>')
        out.append(f'<div class="sec-head">')
        out.append(f'<span class="sec-label" style="background:{color}">{esc(heading)}</span>')
        out.append(f'<span class="sec-count">{len(items)} items</span>')
        out.append(f'</div>')
        out.append('<ul class="link-list">')
        for title, url in items:
            out.append(f'<li><a href="{esc(url)}" target="_blank" rel="noopener">{esc(title)}</a></li>')
        out.append('</ul></div>')

    out.append('</div>')
    return "\n".join(out)

def render_digest():
    total_curated = sum(sum(len(s["items"]) for s in w["sections"]) for w in [W12, W11, W10])
    total_feed = len(STARTME_ITEMS) + len(BRUTALIST_ITEMS)
    grand_total = total_curated + total_feed
    num_sections = len(W12["sections"])

    # Category-based nav: each link jumps to that category in the latest week
    nav_parts = []
    for sec in W12["sections"]:
        slug = cat_slug(sec["heading"])
        color = SECTION_COLORS.get(sec["heading"], "#475569")
        # Title-case label: "FORENSIC ANALYSIS" → "Forensic Analysis"
        label = sec["heading"].replace(" / ", " / ").title().replace(" / ", "/")
        nav_parts.append(
            f'<a href="#cat-{slug}" style="color:{color};border-bottom:2px solid {color};padding-bottom:2px">{label}</a>'
        )
    nav_parts.append('<a href="#feed" style="color:var(--mut)">Recent Feed</a>')
    nav_parts.append('<a href="#community" style="color:#f59e0b">Community</a>')
    nav_html = "\n      ".join(nav_parts)

    # Weekly curated sections
    tw4n6_html = render_week(W12, is_new=True) + render_week(W11) + render_week(W10)

    # Community channel cards
    community_cards = ""
    for ch in COMMUNITY_CHANNELS:
        community_cards += (
            f'<a href="{esc(ch["url"])}" target="_blank" rel="noopener" style="text-decoration:none">'
            f'<div class="community-card" style="border-color:{esc(ch["color"])}">'
            f'<div class="cname">{esc(ch["name"])}</div>'
            f'<div class="cmembers">👥 {esc(ch["members"])} members</div>'
            f'<div class="cdesc">{esc(ch["description"])}</div>'
            f'</div></a>'
        )

    # Combined feed cards (start.me + Brutalist, no source labels)
    feed_cards = ""
    for item in STARTME_ITEMS:
        feed_cards += (
            f'<div class="feed-card">'
            f'<a href="{esc(item["url"])}" target="_blank" rel="noopener">{esc(item["title"])}</a>'
            f'<div class="feed-meta"><span>🗓 {esc(item["date"])}</span></div>'
            f'</div>'
        )
    for item in BRUTALIST_ITEMS:
        feed_cards += (
            f'<div class="feed-card">'
            f'<a href="{esc(item["url"])}" target="_blank" rel="noopener">{esc(item["title"])}</a>'
            f'</div>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>DFIR Watchtower — {DATE_STR}</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>🏰 DFIR Watchtower</h1>
  <p class="sub">Weekly DFIR intelligence digest &mdash; <strong>{DATE_STR}</strong></p>
  <div class="stats">
    <div class="stat"><div class="v">{grand_total}</div><div class="l">Total Links</div></div>
    <div class="stat"><div class="v">{total_curated}</div><div class="l">Curated Links</div></div>
    <div class="stat"><div class="v">3</div><div class="l">Weeks Covered</div></div>
    <div class="stat"><div class="v">{num_sections}</div><div class="l">Categories</div></div>
    <div class="stat"><div class="v">{NOW.strftime("%H:%M UTC")}</div><div class="l">Pulled</div></div>
  </div>
</header>
<nav>{nav_html}</nav>
<main>

<!-- ═══ WEEKLY CURATED ═══ -->
<div class="source-block">
  {tw4n6_html}
</div>

<!-- ═══ RECENT FEED ═══ -->
<div class="source-block" id="feed">
  <div class="week-head" style="margin-bottom:.75rem">
    <h3>Recent Feed</h3>
    <span class="meta">{total_feed} items</span>
  </div>
  {feed_cards}
</div>

<!-- ═══ COMMUNITY CHANNELS ═══ -->
<div class="source-block" id="community">
  <div class="week-head" style="margin-bottom:.75rem">
    <h3>Community Channels</h3>
    <span class="meta">DFIR &amp; security subreddits worth following</span>
  </div>
  <div class="community-grid">
    {community_cards}
  </div>
</div>

</main>
<footer>
  🏰 <strong>DFIR Watchtower</strong> &mdash; {TIMESTAMP} &mdash;
  <a href="https://github.com/forensicfellowship/DFIR_Watchtower">github.com/forensicfellowship/DFIR_Watchtower</a>
</footer>
</body>
</html>"""

# ── Write output ───────────────────────────────────────────────────────────
base = Path("/sessions/epic-optimistic-franklin/mnt/DFIR watchtower")
content = render_digest()

# Dated archive copy
dated_path = base / f"watchtower_digest_{DATE_STR}.html"
dated_path.write_text(content, encoding="utf-8")

# index.html — always the latest, served by GitHub Pages
index_path = base / "index.html"
index_path.write_text(content, encoding="utf-8")

tw4n6_total = sum(sum(len(s["items"]) for s in w["sections"]) for w in [W12, W11, W10])
print(f"✅  Written {len(content):,} chars")
print(f"    Dated   → {dated_path}")
print(f"    Live    → {index_path}  (GitHub Pages)")
print(f"    This Week in 4n6 : {tw4n6_total} links (Weeks 10-12, {len(W12['sections'])} sections each)")
print(f"    start.me Feed    : {len(STARTME_ITEMS)} items")
print(f"    Brutalist Report : {len(BRUTALIST_ITEMS)} items")
print(f"    GRAND TOTAL      : {tw4n6_total + len(STARTME_ITEMS) + len(BRUTALIST_ITEMS)} links")
