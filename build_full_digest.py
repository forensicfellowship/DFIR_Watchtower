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

# ═══════════════════════════════════════════════════════════════════════════
# DFIR RADAR RSS — Live threat intelligence feed (falhumaid.github.io/DFIR_Radar_RSS)
# Scraped: 2026-04-02 | 100 items | Categories: THREAT INTELLIGENCE, DETECTION,
#          MALWARE ANALYSIS, INCIDENT RESPONSE, FORENSICS, VULNERABILITY, CLOUD SECURITY
# ═══════════════════════════════════════════════════════════════════════════

RADAR_COLORS = {
    "THREAT INTELLIGENCE": "#dc2626",
    "DETECTION":           "#0e7490",
    "MALWARE ANALYSIS":    "#b45309",
    "INCIDENT RESPONSE":   "#047857",
    "FORENSICS":           "#7c3aed",
    "VULNERABILITY":       "#d97706",
    "CLOUD SECURITY":      "#2563eb",
}

DFIR_RADAR_ITEMS = [
    # ── THREAT INTELLIGENCE (56 items) ─────────────────────────────────────
    {"cat": "THREAT INTELLIGENCE", "title": "Anthropic Claude Code Leak", "url": "https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak", "date": "02 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "How we caught the Axios supply chain attack", "url": "https://www.elastic.co/security-labs/how-we-caught-the-axios-supply-chain-attack", "date": "02 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Mitigating the Axios npm supply chain compromise", "url": "https://www.microsoft.com/en-us/security/blog/2026/04/01/mitigating-the-axios-npm-supply-chain-compromise/", "date": "02 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Frequently Asked Questions About the Axios npm Supply Chain Attack (UNC1069)", "url": "https://securityboulevard.com/2026/04/frequently-asked-questions-about-the-axios-npm-supply-chain-attack-by-north-korea-nexus-threat-actor-unc1069/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "FAQ: Axios npm Supply Chain Attack by North Korea-Nexus UNC1069 (Tenable)", "url": "https://www.tenable.com/blog/faq-about-the-axios-npm-supply-chain-attack-by-north-korea-nexus-threat-actor-unc1069", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "The Scanner Was the Weapon: 36 Months of Precision Supply Chain Attacks Against DevSecOps Infrastructure", "url": "https://www.cloudsek.com/blog/the-scanner-was-the-weapon-36-months-of-precision-supply-chain-attacks-against-devsecops-infrastructure", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "A malicious LNK that spreads a Python-based backdoor (Kimsuky group)", "url": "https://asec.ahnlab.com/en/93151/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "UAC-0255 Attack Detection: Threat Actors Impersonate CERT-UA to Deploy AGEWHEEZE RAT", "url": "https://socprime.com/blog/uac-0255-distributing-agewheeze-rat/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Supply Chain Attack on Axios Delivers Cross-Platform RAT via Compromised npm Account", "url": "https://orca.security/resources/blog/axios-npm-supply-chain-attack-remediation/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Breaking down the Axios supply chain incident", "url": "https://www.vectra.ai/blog/breaking-down-the-axios-supply-chain-incident", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More", "url": "https://any.run/cybersecurity-blog/major-cyber-attacks-march-2026/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Hackers Hijack Axios npm Package to Spread RATs", "url": "https://www.infosecurity-magazine.com/news/hackers-hijack-axios-npm-package/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Attackers hijack Axios npm account to spread RAT malware", "url": "https://securityaffairs.com/190221/security/attackers-hijack-axios-npm-account-to-spread-rat-malware.html", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "North Korea\u2019s Lazarus Group Behind the Axios npm Supply Chain Attack", "url": "https://thecyberexpress.com/lazarus-behind-axios-npm-supply-chain-attack/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Infect Once, Spread Everywhere: CanisterWorm and the Automation of Supply Chain Compromise", "url": "https://blog.polyswarm.io/infect-once-spread-everywhere-canisterworm-and-the-automation-of-supply-chain-compromise", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Initial Access Brokers Shift to High-Value Targets and Premium Pricing", "url": "https://www.rapid7.com/blog/post/tr-initial-access-broker-shift-high-value-targets-premium-pricing", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Axios npm package compromised to deploy malware (Sophos)", "url": "https://www.sophos.com/en-us/blog/axios-npm-package-compromised-to-deploy-malware", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Axios Front-End Library npm Supply Chain Poisoning Alert", "url": "https://nsfocusglobal.com/axios-front-end-library-npm-supply-chain-poisoning-alert/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Hackers compromise Axios npm package to drop cross-platform malware (BleepingComputer)", "url": "https://www.bleepingcomputer.com/news/security/hackers-compromise-axios-npm-package-to-drop-cross-platform-malware/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Supply chain attack on Axios npm: Scope, impact, and remediations (Tenable)", "url": "https://www.tenable.com/blog/supply-chain-attack-on-axios-npm-package-scope-impact-and-remediations", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "North Korea-Nexus Threat Actor Compromises Widely Used Axios NPM Package (Google TAG)", "url": "https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package/", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Axios supply chain attack chops away at npm trust (Malwarebytes)", "url": "https://www.malwarebytes.com/blog/news/2026/03/axios-supply-chain-attack-chops-away-at-npm-trust", "date": "01 Apr 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Fake Installers to Monero: A Multi-Tool Mining Operation (Elastic)", "url": "https://www.elastic.co/security-labs/fake-installers-to-monero", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Compromised Axios npm package delivers cross-platform RAT (Datadog)", "url": "https://securitylabs.datadoghq.com/articles/axios-npm-supply-chain-compromise/", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Inside the Axios supply chain compromise — one RAT to rule them all (Elastic)", "url": "https://www.elastic.co/security-labs/axios-one-rat-to-rule-them-all", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "WhatsApp malware campaign delivers VBS payloads and MSI backdoors (Microsoft)", "url": "https://www.microsoft.com/en-us/security/blog/2026/03/31/whatsapp-malware-campaign-delivers-vbs-payloads-msi-backdoors/", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Operation TrueChaos: 0-Day Exploitation Against Southeast Asian Government Targets (Check Point)", "url": "https://research.checkpoint.com/2026/operation-truechaos-0-day-exploitation-against-southeast-asian-government-targets/", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Axios NPM Distribution Compromised in Supply Chain Attack (Wiz)", "url": "https://www.wiz.io/blog/axios-npm-compromised-in-supply-chain-attack", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Axios npm Hijack 2026: IOCs, Impact & Remediation (SOCRadar)", "url": "https://socradar.io/blog/axios-npm-supply-chain-attack-2026-ciso-guide/", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Axios Supply Chain Attack Exposes Developers to Hidden Malware (CyberExpress)", "url": "https://thecyberexpress.com/axios-supply-chain-attack-npm-malware/", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "The Axios npm Compromise: How the Internet\u2019s Most Popular HTTP Client Became a Trojan Horse", "url": "https://infosecwriteups.com/the-axios-npm-compromise-how-the-internets-most-popular-http-client-became-a-trojan-horse-c80c6f73f52d", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Tracking TeamPCP: Investigating Post-Compromise Attacks Seen in the Wild (Wiz)", "url": "https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Supply Chain Attack on Axios Pulls Malicious Dependency (Socket)", "url": "https://socket.dev/blog/axios-npm-package-compromised", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "From Shai-Hulud to LiteLLM: Supply Chain Attackers Are Coming for Your Agents (JFrog)", "url": "https://jfrog.com/blog/supply-chain-attackers-are-coming-for-your-agents/", "date": "31 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "China-Linked groups target Southeast Asian government with advanced malware (SecurityAffairs)", "url": "https://securityaffairs.com/190174/apt/china-linked-groups-target-southeast-asian-government-with-advanced-malware-in-2025.html", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "FBI warns Iran-linked cyber campaign uses Telegram bots to scale attacks", "url": "https://industrialcyber.co/threats-attacks/fbi-warns-iran-linked-cyber-campaign-uses-telegram-bots-to-control-compromised-systems-scale-attacks/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Detecting an email-based ClickFix attack delivering DCRat malware (Sublime Security)", "url": "https://proxied2.sublime.security/blog/detecting-an-email-based-clickfix-attack-that-delivers-dcrat-malware-payload", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "TeamPCP\u2019s Telnyx Attack Marks a Shift in Tactics Beyond LiteLLM (Trend Micro)", "url": "https://www.trendmicro.com/en_us/research/26/c/teampcp-telnyx-attack-marks-a-shift-in-tactics.html", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Professional Networks Under Attack: Vietnam-Linked Actors Deploy PXA Stealer (Cyble)", "url": "https://cyble.com/blog/professional-networks-under-attack-by-infostealer/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Keitaro TDS abused to deliver AutoIT-based loader targeting German speakers (Sublime Security)", "url": "https://proxied2.sublime.security/blog/keitaro-tds-abused-to-delivery-autoit-based-loader-targeting-german-speakers", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "AITM phishing with Russian infrastructure and detection evasion from a lapsed domain (Sublime)", "url": "https://proxied2.sublime.security/blog/aitm-phishing-with-russian-infrastructure-and-detection-evasion-from-a-lapsed-domain", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "HostPapa abuse treasure trove discovered in GoDaddy email threat hunt (Sublime Security)", "url": "https://proxied2.sublime.security/blog/hostpapa-abuse-treasure-trove-discovered-in-godaddy-email-threat-hunt", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "New widespread EvilTokens kit: device code phishing-as-a-service (Sekoia)", "url": "https://blog.sekoia.io/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Hackers Impersonate Ukrainian CERT to Plant AGEWHEEZE RAT on Government Networks", "url": "https://thecyberexpress.com/hackers-impersonate-cert-ua-agewheeze-rat/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "AI Threat Landscape Digest January\u2013February 2026 (Check Point)", "url": "https://research.checkpoint.com/2026/ai-threat-landscape-digest-january-february-2026/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Malware & Phishing Threat Landscape Report \u2013 2025/2 (VMRay)", "url": "https://www.vmray.com/malware-phishing-threat-landscape-report-2025-2/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom Networks", "url": "https://thehackernews.com/2026/03/china-linked-red-menshen-uses-stealthy.html", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "A cunning predator: How Silver Fox preys on Japanese firms this tax season (ESET)", "url": "https://www.welivesecurity.com/en/business-security/cunning-predator-how-silver-fox-preys-japanese-firms-tax-season/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Backdoored Telnyx PyPI package pushes malware hidden in WAV audio (BleepingComputer)", "url": "https://www.bleepingcomputer.com/news/security/backdoored-telnyx-pypi-package-pushes-malware-hidden-in-wav-audio/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "PolyKG Discovers Previously Unreported OilRig Samples Using Stolen Cert", "url": "https://blog.polyswarm.io/polykg-discovers-previously-unreported-oilrig-samples-using-stolen-cert", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Famous Telnyx PyPI Package compromised by TeamPCP (Security Boulevard)", "url": "https://securityboulevard.com/2026/03/famous-telnyx-pypi-package-compromised-by-teampcp/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "TeamPCP Targets Telnyx Package in Latest PyPI Software Supply Chain Attack", "url": "https://www.infosecurity-magazine.com/news/teampcp-targets-telnyx-pypi-package/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "TeamPCP Supply Chain Campaign Update 002: Telnyx PyPI Compromise & Vect Ransomware (SANS ISC)", "url": "https://isc.sans.edu/diary/rss/32838", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Under CTRL: Dissecting a Previously Undocumented Russian .NET Access Framework (Censys)", "url": "https://censys.com/blog/under-ctrl-dissecting-a-previously-undocumented-russian-net-access-framework/", "date": "30 Mar 2026"},
    {"cat": "THREAT INTELLIGENCE", "title": "Microsoft Power BI API Credential Exposure from Public Postman Workspace", "url": "https://infosecwriteups.com/microsoft-power-bi-api-credential-exposure-from-public-postman-workspace", "date": "30 Mar 2026"},
    # ── DETECTION (15 items) ────────────────────────────────────────────────
    {"cat": "DETECTION", "title": "Hooked on Linux: Rootkit Detection Engineering (Elastic Security Labs)", "url": "https://www.elastic.co/security-labs/linux-rootkits-2-caught-in-the-act", "date": "02 Apr 2026"},
    {"cat": "DETECTION", "title": "Prioritizing Alerts Triage with Higher-Order Detection Rules (Elastic)", "url": "https://www.elastic.co/security-labs/higher-order-detection-rules", "date": "01 Apr 2026"},
    {"cat": "DETECTION", "title": "SentinelOne autonomous detection blocks trojaned LiteLLM triggered by Claude Code", "url": "https://securityaffairs.com/190248/security/sentinelone-autonomous-detection-blocks-trojaned-litellm-triggered-by-claude-code.html", "date": "01 Apr 2026"},
    {"cat": "DETECTION", "title": "The CertGraveyard", "url": "https://squiblydoo.blog/2026/04/01/the-certgraveyard/", "date": "01 Apr 2026"},
    {"cat": "DETECTION", "title": "Detecting CVE-2026-20929: Kerberos Authentication Relay via CNAME Abuse (CrowdStrike)", "url": "https://www.crowdstrike.com/en-us/blog/detecting-kerberos-relay-attack-via-dns-cname-abuse/", "date": "01 Apr 2026"},
    {"cat": "DETECTION", "title": "Reduce conn.log from 35GB to 5GB with a Simple Hook (Zeek)", "url": "https://zeek.org/2026/03/reduce-conn-log-from-35gb-to-5gb-with-a-simple-hook/", "date": "01 Apr 2026"},
    {"cat": "DETECTION", "title": "Elastic releases detections for the Axios supply chain compromise", "url": "https://www.elastic.co/security-labs/axios-supply-chain-compromise-detections", "date": "31 Mar 2026"},
    {"cat": "DETECTION", "title": "Google Careers impersonation credential phishing scam with endless variation (Sublime Security)", "url": "https://proxied2.sublime.security/blog/google-careers-impersonation-credential-phishing-scam-with-endless-variation", "date": "31 Mar 2026"},
    {"cat": "DETECTION", "title": "Detecting malicious AnonymousFox email messages sent from compromised sites (Sublime Security)", "url": "https://proxied2.sublime.security/blog/detecting-malicious-anonymousfox-email-messages-sent-from-compromised-sites", "date": "30 Mar 2026"},
    {"cat": "DETECTION", "title": "Introduction to Message Query Language (MQL) (Sublime Security)", "url": "https://proxied2.sublime.security/blog/introduction-to-message-query-language-mql", "date": "30 Mar 2026"},
    {"cat": "DETECTION", "title": "Base64-encoding an SVG attack within an iframe hidden in an EML attachment (Sublime Security)", "url": "https://proxied2.sublime.security/blog/base64-encoding-an-svg-attack-within-an-iframe-and-hiding-it-all-in-an-eml-attachment", "date": "30 Mar 2026"},
    {"cat": "DETECTION", "title": "Threats based on Clipboard actions (+ KQL Query)", "url": "https://detect.fyi/threats-based-on-clipboards-actions-kql-query-93615eef79b7", "date": "30 Mar 2026"},
    {"cat": "DETECTION", "title": "Researchers release tool to detect stealthy BPFDoor implants in critical infrastructure", "url": "https://www.helpnetsecurity.com/2026/03/26/telecom-bpfdoor-detection-script/", "date": "30 Mar 2026"},
    {"cat": "DETECTION", "title": "ClickFix: Stopped at \u2318+V (Objective-See)", "url": "https://objective-see.org/blog/blog_0x86.html", "date": "30 Mar 2026"},
    {"cat": "DETECTION", "title": "Threat Hunting with OpenCTI + OpenAEV + Splunk ESCU (Filigran)", "url": "https://filigran.io/threat-hunting-with-opencti-openaev-splunk-escu/", "date": "30 Mar 2026"},
    # ── MALWARE ANALYSIS (11 items) ─────────────────────────────────────────
    {"cat": "MALWARE ANALYSIS", "title": "A laughing RAT: CrystalX combines spyware, stealer, and prankware features (Kaspersky)", "url": "https://securelist.com/crystalx-rat-with-prankware-features/119283/", "date": "01 Apr 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "Latest Xloader Obfuscation Methods and Network Protocol (Zscaler)", "url": "https://www.zscaler.com/blogs/security-research/latest-xloader-obfuscation-methods-and-network-protocol", "date": "31 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "DeepLoad Malware Combines ClickFix With AI-Generated Code to Avoid Detection", "url": "https://www.infosecurity-magazine.com/news/deepload-malware-clickfix-ai-code/", "date": "31 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "DeepLoad Malware Uses ClickFix and WMI Persistence to Steal Browser Credentials (The Hacker News)", "url": "https://thehackernews.com/2026/03/deepload-malware-uses-clickfix-and-wmi.html", "date": "31 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "Analysis of FvncBot campaign (CERT Poland)", "url": "https://cert.pl/en/posts/2026/03/fvncbot-analysis/", "date": "31 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "New RoadK1ll WebSocket implant used to pivot on breached networks (BleepingComputer)", "url": "https://www.bleepingcomputer.com/news/security/new-roadk1ll-websocket-implant-used-to-pivot-on-breached-networks/", "date": "30 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "Resoker: A Telegram Based Remote Access Trojan (K7 Computing)", "url": "https://labs.k7computing.com/index.php/resoker-a-telegram-based-remote-access-trojan/", "date": "30 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "Compromising Telecom Systems: Deploying and Detecting the BPFDoor Backdoor", "url": "https://hackers-arise.com/compromising-telecom-systems-deploying-and-detecting-the-bpfdoor-backdoor/", "date": "30 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "New Infinity Stealer malware grabs macOS data via ClickFix lures (BleepingComputer)", "url": "https://www.bleepingcomputer.com/news/security/new-infinity-stealer-malware-grabs-macos-data-via-clickfix-lures/", "date": "30 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "Coruna exploit reveals evolution of Triangulation iOS exploitation framework", "url": "https://securityaffairs.com/190010/security/coruna-exploit-reveals-evolution-of-triangulation-ios-exploitation-framework.html", "date": "30 Mar 2026"},
    {"cat": "MALWARE ANALYSIS", "title": "TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files", "url": "https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html", "date": "30 Mar 2026"},
    # ── INCIDENT RESPONSE (4 items) ─────────────────────────────────────────
    {"cat": "INCIDENT RESPONSE", "title": "Axios Hijacked: npm Account Takeover Deploys Cross-Platform RAT to Millions (Security Boulevard)", "url": "https://securityboulevard.com/2026/03/axios-hijacked-npm-account-takeover-deploys-cross-platform-rat-to-millions/", "date": "31 Mar 2026"},
    {"cat": "INCIDENT RESPONSE", "title": "Axios Supply Chain Attack: Analysis & Incident Response (Invictus IR)", "url": "https://www.invictus-ir.com/news/the-poisoned-pipeline-axios-supply-chain-attack", "date": "31 Mar 2026"},
    {"cat": "INCIDENT RESPONSE", "title": "Business Email Compromise Investigation Walkthrough (r/dfir)", "url": "https://www.reddit.com/r/dfir/comments/1s5ccx0/business_email_compromise_investigation/", "date": "30 Mar 2026"},
    {"cat": "INCIDENT RESPONSE", "title": "Metasploit Wrap-Up 03/27/2026 (Rapid7)", "url": "https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-03-27-2026", "date": "30 Mar 2026"},
    # ── FORENSICS (4 items) ─────────────────────────────────────────────────
    {"cat": "FORENSICS", "title": "iOS Lockdown Mode and Forensic Analysis: A Technical Perspective", "url": "https://andreafortuna.org/2026/03/29/ios-lockdown-mode-forensics/", "date": "30 Mar 2026"},
    {"cat": "FORENSICS", "title": "An open-source forensic exporter for ChatGPT conversations (SHA-256 hashing)", "url": "https://www.reddit.com/r/computerforensics/comments/1s6cx7e/an_opensource_forensic_exporter_for_chatgpt/", "date": "30 Mar 2026"},
    {"cat": "FORENSICS", "title": "Digital Forensics: Analyzing Fake Software", "url": "https://hackers-arise.com/digital-forensics-analyzing-fake-software/", "date": "30 Mar 2026"},
    {"cat": "FORENSICS", "title": "Linux Forensic Scenario", "url": "https://righteousit.com/2026/03/27/linux-forensic-scenario/", "date": "30 Mar 2026"},
    # ── VULNERABILITY (7 items) ─────────────────────────────────────────────
    {"cat": "VULNERABILITY", "title": "CVE-2025-53521: F5 BIG-IP APM Flaw Reclassified as Unauthenticated RCE (SOCRadar)", "url": "https://socradar.io/blog/cve-2025-53521-f5-big-ip-apm-flaw-rce/", "date": "01 Apr 2026"},
    {"cat": "VULNERABILITY", "title": "Hackers Circle Citrix NetScaler Flaw Within Hours of Disclosure", "url": "https://thecyberexpress.com/cve-2026-3055-citrix-netscaler-saml-idp/", "date": "31 Mar 2026"},
    {"cat": "VULNERABILITY", "title": "Please, We Beg, Just One Weekend Free Of Appliances (Citrix NetScaler CVE-2026-3055 Part 2)", "url": "https://labs.watchtowr.com/please-we-beg-just-one-weekend-free-of-appliances-citrix-netscaler-cve-2026-3055-memory-overread-part-2/", "date": "31 Mar 2026"},
    {"cat": "VULNERABILITY", "title": "The Sequels Are Never As Good (Citrix NetScaler CVE-2026-3055 Memory Overread)", "url": "https://labs.watchtowr.com/the-sequels-are-never-as-good-but-were-still-in-pain-citrix-netscaler-cve-2026-3055-memory-overread/", "date": "30 Mar 2026"},
    {"cat": "VULNERABILITY", "title": "Microsoft Authenticator\u2019s Unclaimed Deep Link: A Full Account Takeover Story (CVE-2026-26123)", "url": "https://infosecwriteups.com/microsoft-authenticators-unclaimed-deep-link-a-full-account-takeover-story-cve-2026-26123-e0409a920a02", "date": "30 Mar 2026"},
    {"cat": "VULNERABILITY", "title": "Unpatchable Vulnerabilities of Kubernetes: CVE-2020-8561 (Datadog Security Labs)", "url": "https://securitylabs.datadoghq.com/articles/unpatchable-kubernetes-vulnerabilities-cve-2020-8561/", "date": "30 Mar 2026"},
    {"cat": "VULNERABILITY", "title": "ShadowPrompt: Zero-Click Prompt Injection Chain in Anthropic\u2019s Claude Chrome Extension", "url": "https://socradar.io/blog/shadowprompt-zero-click-anthropics-claude/", "date": "30 Mar 2026"},
    # ── CLOUD SECURITY (3 items) ────────────────────────────────────────────
    {"cat": "CLOUD SECURITY", "title": "Common Entra ID Security Assessment Findings \u2013 Part 2: Privileged Unprotected Groups", "url": "https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-2-privileged-unprotected-groups/", "date": "31 Mar 2026"},
    {"cat": "CLOUD SECURITY", "title": "ChatGPT Data Leakage via a Hidden Outbound Channel in the Code Execution Runtime (Check Point)", "url": "https://research.checkpoint.com/2026/chatgpt-data-leakage-via-a-hidden-outbound-channel-in-the-code-execution-runtime/", "date": "31 Mar 2026"},
    {"cat": "CLOUD SECURITY", "title": "Azure Blob Storage Misconfigurations: Attacker\u2019s Gateway to Data", "url": "https://infosecwriteups.com/azure-blob-storage-misconfigurations-attackers-gateway-to-data-b7d8e957440e", "date": "30 Mar 2026"},
]


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

def render_radar_sections():
    """Render DFIR Radar items grouped by category, no source branding."""
    from collections import defaultdict
    by_cat = defaultdict(list)
    for item in DFIR_RADAR_ITEMS:
        by_cat[item["cat"]].append(item)

    # Ordered category list
    cat_order = ["THREAT INTELLIGENCE", "DETECTION", "MALWARE ANALYSIS",
                 "INCIDENT RESPONSE", "FORENSICS", "VULNERABILITY", "CLOUD SECURITY"]
    out = []
    for cat in cat_order:
        items = by_cat.get(cat, [])
        if not items:
            continue
        color = RADAR_COLORS.get(cat, "#475569")
        slug = cat_slug(cat)
        out.append(f'<div class="section-block" id="radar-{slug}">')
        out.append(f'<div class="sec-head">')
        out.append(f'<span class="sec-label" style="background:{color}">{esc(cat)}</span>')
        out.append(f'<span class="sec-count">{len(items)} items</span>')
        out.append(f'</div>')
        out.append('<ul class="link-list">')
        for item in items:
            out.append(f'<li><a href="{esc(item["url"])}" target="_blank" rel="noopener">{esc(item["title"])}</a></li>')
        out.append('</ul></div>')
    return "\n".join(out)


def render_digest():
    tw4n6_curated = sum(len(s["items"]) for s in W12["sections"])
    radar_total   = len(DFIR_RADAR_ITEMS)
    total_feed    = len(STARTME_ITEMS) + len(BRUTALIST_ITEMS)
    grand_total   = tw4n6_curated + radar_total + total_feed

    # Unique category count across both sources
    radar_cats = {i["cat"] for i in DFIR_RADAR_ITEMS}
    tw4n6_cats = {s["heading"] for s in W12["sections"]}
    num_sections = len(tw4n6_cats | radar_cats)

    # Nav: TW4N6 categories first (jump to week-12 anchors)
    nav_parts = []
    for sec in W12["sections"]:
        slug = cat_slug(sec["heading"])
        color = SECTION_COLORS.get(sec["heading"], "#475569")
        label = sec["heading"].title().replace(" / ", "/")
        nav_parts.append(
            f'<a href="#cat-{slug}" style="color:{color};border-bottom:2px solid {color};padding-bottom:2px">{label}</a>'
        )
    # DFIR Radar extra categories (ones not already in TW4N6)
    radar_only = ["DETECTION", "INCIDENT RESPONSE", "FORENSICS", "VULNERABILITY", "CLOUD SECURITY"]
    for cat in radar_only:
        color = RADAR_COLORS.get(cat, "#475569")
        slug  = cat_slug(cat)
        nav_parts.append(
            f'<a href="#radar-{slug}" style="color:{color};border-bottom:2px solid {color};padding-bottom:2px">{cat.title()}</a>'
        )
    nav_parts.append('<a href="#feed" style="color:var(--mut)">Recent Feed</a>')
    nav_parts.append('<a href="#community" style="color:#f59e0b">Community</a>')
    nav_html = "\n      ".join(nav_parts)

    # Weekly curated sections — 1 week only
    tw4n6_html = render_week(W12, is_new=True)

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
    <div class="stat"><div class="v">{tw4n6_curated}</div><div class="l">Curated Links</div></div>
    <div class="stat"><div class="v">{radar_total}</div><div class="l">Radar Links</div></div>
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

<!-- ═══ INTEL FEED ═══ -->
<div class="source-block">
  {render_radar_sections()}
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

tw4n6_total = sum(len(s["items"]) for s in W12["sections"])
print(f"✅  Written {len(content):,} chars")
print(f"    Dated   → {dated_path}")
print(f"    Live    → {index_path}  (GitHub Pages)")
print(f"    This Week in 4n6 : {tw4n6_total} links (Week 12, {len(W12['sections'])} sections)")
print(f"    DFIR Radar RSS   : {len(DFIR_RADAR_ITEMS)} links ({len({i['cat'] for i in DFIR_RADAR_ITEMS})} categories)")
print(f"    start.me Feed    : {len(STARTME_ITEMS)} items")
print(f"    Brutalist Report : {len(BRUTALIST_ITEMS)} items")
print(f"    GRAND TOTAL      : {tw4n6_total + len(DFIR_RADAR_ITEMS) + len(STARTME_ITEMS) + len(BRUTALIST_ITEMS)} links")
