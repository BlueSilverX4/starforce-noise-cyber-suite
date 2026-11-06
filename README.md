# ⚡ StarForce Noise Cyber Suite

**A Modular Defensive Telemetry, SIEM Testing, and Threat-Hunting Framework**

The **StarForce Noise Cyber Suite** is a modular, defense-in-depth cybersecurity telemetry and threat-hunting framework built on a bare-metal Kali Purple node running on an HP Pavilion 23.

Inspired by tactical science-fiction monitoring systems, the project integrates simulated network noise generation, Zeek network analysis, a containerized Cowrie SSH honeypot, and centralized security telemetry visualization through Grafana and Loki.

The objective is to create a controlled defensive environment for testing SIEM ingestion pipelines, analyzing network activity, capturing honeypot interactions, and visualizing security events.

**Focus Areas:** SIEM Engineering · Network Monitoring · Threat Hunting · Honeypot Deployment · Telemetry Collection · Security Visualization

---

## 🏛️ Repository Architecture

```text
StarForce-Noise-Cyber-Suite/
│
├── 01-noise-rate-siem/
│   ├── decoders/
│   │   └── noise_decoder.xml
│   ├── rules/
│   │   └── noise_rules.xml
│   └── scripts/
│       ├── noise_generator.py
│       └── noise_injector.py
│
├── 02-wave-ids-wireless/
│   ├── configs/
│   ├── *.log
│   ├── rules/
│   └── zeek_scripts/
│       └── wave_anomaly.zeek
│
├── 03-black-hole-honeypot/
│   ├── config/
│   ├── cowrie-logs/
│   │   └── cowrie.json
│   └── docker-compose.yml
│
├── 04_dashboard/
│   └── noise_terminal_dashboard.json
│
└── screenshots/
    ├── 01_wazuh_noise_decoded.png
    ├── 02_deploy_noise_injector.png
    ├── 03_zeek_wave_anomaly.png
    ├── 04_decoding_testing_cowie.png
    ├── 05_noise_terminal.png
    ├── 06_stream_all_honeypot_logs_dashboard.png
    ├── 07_total_attack_attempts_over_time_dashboard.png
    ├── 08_top_five_attacker_source_ips_dashboard.png
    └── 09_successful_unauthorized_logins_counter_dashboard.png
```

---

## 🛡️ Core Modules & Capabilities

### 1. Noise Rate SIEM

<text>**Directory:** `01-noise-rate-siem/`</text>

**Purpose:** Simulates and ingests high-frequency network noise events to exercise SIEM ingestion pipelines and anomaly-detection thresholds.

**Simulated event categories:**

- `port_scan` — Simulated port-scanning activity.
- `packet_storm` — High-volume simulated packet activity.
- `brute_force` — Repeated authentication-attempt events.
- `rogue_beacon` — Simulated beacon-like telemetry.

**Components:**

| File | Responsibility |
|---|---|
| `noise_decoder.xml` | Custom Wazuh decoder for noise simulation events. |
| `noise_rules.xml` | Custom Wazuh alert thresholds and event classifications. |
| `noise_generator.py` | Background event simulation engine. |
| `noise_injector.py` | Event generation and logging script. |

**Defensive objective:** Validate event ingestion, decoder behavior, rule matching, and alert generation under simulated event volume.

### 2. Wave IDS Wireless

<text>**Directory:** `02-wave-ids-wireless/`</text>

**Purpose:** Network analysis layer powered by Zeek, designed to collect protocol telemetry and identify suspicious traffic patterns.

**Components:**

- `wave_anomaly.zeek` — Custom Zeek script for anomalous wave-pattern detection.
- `configs/` — Zeek configuration files.
- `rules/` — Network packet filtering rules.
- Protocol logs — Structured network activity records.

**Documented telemetry includes:**

| Log | Purpose |
|---|---|
| `conn.log` | Network connection activity. |
| `dns.log` | DNS request and response telemetry. |
| `dhcp.log` | DHCP activity. |
| `ssl.log` | TLS/SSL connection metadata. |
| `x509.log` | Certificate-related telemetry. |

**Defensive objective:** Analyze network behavior and identify anomalies through protocol-level visibility.

### 3. Black Hole Honeypot

<text>**Directory:** `03-black-hole-honeypot/`</text>

**Purpose:** Deploys a containerized Cowrie SSH honeypot using Docker Compose, with the documented service mapped to port `2222`.

**Components:**

- `config/` — Honeypot configuration overrides.
- `cowrie-logs/cowrie.json` — Structured JSON session telemetry.
- `docker-compose.yml` — Container deployment configuration.

**Documented telemetry includes:**

- Client version and SSH handshake information.
- HASSH fingerprint information.
- Submitted authentication credentials.
- Terminal dimensions.
- Interactive commands, including `exit`.
- TTY session telemetry.

**Defensive objective:** Capture and examine unauthorized SSH interaction attempts within a controlled honeypot environment.

> **Security note:** Honeypot credentials and session contents may be sensitive. Use synthetic test credentials and protect collected logs. Never reuse real passwords or expose captured credentials in public repository screenshots.

### 4. Operational Dashboard

<text>**Directory:** `04_dashboard/`</text>

**Purpose:** Provides the visualization layer for centralized security telemetry through Grafana and Loki.

**Dashboard model:**

`noise_terminal_dashboard.json`

**Documented panels:**

1. Real-time stream of incoming honeypot events.
2. Attack-volume time-series aggregations over 24-hour windows.
3. Top five attacker source IP addresses.
4. Counter for successful unauthorized-login events.

**Defensive objective:** Provide a centralized operational view of simulated network activity, honeypot interactions, and security events.

---

## 🔄 Operational Workflow

```text
     SIMULATED SECURITY EVENTS
                 |
                 v
       +-------------------+
       |   Noise Rate SIEM |
       |   Wazuh Decoders  |
       +---------+---------+
                 |
                 v
       +-------------------+
       |   Wave IDS        |
       |   Zeek Telemetry  |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Black Hole        |
       | Cowrie Honeypot   |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Centralized Log   |
       | Ingestion         |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Grafana / Loki    |
       | Noise Terminal    |
       +-------------------+
```

*This diagram presents the suite's documented functional components. Confirm the actual log-forwarding connections and data sources in the deployed configuration.*

---

## 🛠️ Quick Start & Deployment

### Prerequisites

- Kali Linux / Kali Purple.
- Python 3.
- Docker Engine.
- Docker Compose.
- Wazuh manager with the appropriate custom decoder and rule configuration.
- Zeek.
- Grafana and Loki for dashboard visualization.

### 1. Deploy the Black Hole Honeypot

Navigate to the honeypot module:

```bash
cd 03-black-hole-honeypot
```

Start the Docker Compose deployment:

```bash
docker compose up -d
```

Verify the container status:

```bash
docker compose ps
```

Review container logs:

```bash
docker compose logs --tail=100
```

### 2. Run the Noise Injector

From the repository root, execute:

```bash
sudo python3 01-noise-rate-siem/scripts/noise_injector.py
```

This launches the documented event-injection script.

Monitor the resulting Wazuh events and verify that the custom decoder and rules process the generated records as expected.

### 3. Inspect Zeek Telemetry

Navigate to the network-monitoring module:

```bash
cd 02-wave-ids-wireless
```

Inspect available protocol logs:

```bash
ls -lh *.log
```

Review connection telemetry:

```bash
tail -f conn.log
```

If Zeek writes logs to a different configured directory, use that actual path instead.

### 4. Review Cowrie Honeypot Telemetry

From the repository root:

```bash
tail -f 03-black-hole-honeypot/cowrie-logs/cowrie.json
```

For readable JSON output:

```bash
tail -f 03-black-hole-honeypot/cowrie-logs/cowrie.json | jq .
```

### 5. Import the Grafana Dashboard

1. Open your Grafana instance.
2. Navigate to dashboard import.
3. Import `04_dashboard/noise_terminal_dashboard.json`.
4. Configure the appropriate Loki data source.
5. Verify that the dashboard queries match the labels and JSON fields in your ingested telemetry.

**Important:** Importing the dashboard does not automatically configure Wazuh, Zeek, Cowrie, Alloy, or Loki. The required collection and forwarding pipeline must already be running.

---

## 📸 Dashboard Preview & Verification Evidence

The `screenshots/` directory provides visual evidence of the suite's components and operational testing.

| Screenshot | Evidence |
|---|---|
| `01_wazuh_noise_decoded.png` | Wazuh noise-event decoding. |
| `02_deploy_noise_injector.png` | Noise injector deployment. |
| `03_zeek_wave_anomaly.png` | Zeek anomaly-detection output. |
| `04_decoding_testing_cowie.png` | Cowrie-related decoding test. |
| `05_noise_terminal.png` | Operational dashboard overview. |
| `06_stream_all_honeypot_logs_dashboard.png` | Honeypot event stream visualization. |
| `07_total_attack_attempts_over_time_dashboard.png` | Attack-attempt trend visualization. |
| `08_top_five_attacker_source_ips_dashboard.png` | Source IP aggregation panel. |
| `09_successful_unauthorized_logins_counter_dashboard.png` | Successful-login event counter. |

### Recommended Validation Checklist

- [ ] Confirm Wazuh receives the generated noise events.
- [ ] Verify `noise_decoder.xml` parses the intended event format.
- [ ] Confirm `noise_rules.xml` produces the expected alerts.
- [ ] Verify Zeek generates the expected protocol logs.
- [ ] Confirm the custom `wave_anomaly.zeek` script loads and executes.
- [ ] Verify Cowrie records SSH interaction events.
- [ ] Confirm honeypot JSON telemetry reaches the centralized logging pipeline.
- [ ] Verify Grafana panels display the expected data.
- [ ] Confirm dashboard counters and aggregations match the underlying records.

---

## 🔐 Safe Testing Practices

StarForce Noise Cyber Suite is designed for authorized defensive security testing.

- Generate simulated traffic within a controlled lab.
- Restrict honeypot exposure to interfaces and networks you intend to monitor.
- Avoid exposing SSH honeypot services directly to untrusted networks without appropriate isolation.
- Use synthetic credentials during testing.
- Protect Cowrie session logs and authentication telemetry.
- Validate Wazuh decoders and rules before deploying them into other environments.
- Review dashboard data for accidentally exposed usernames, addresses, or other sensitive information.

---

## 🎯 Project Objectives

StarForce Noise Cyber Suite demonstrates practical defensive security engineering through:

- **SIEM Engineering:** Custom Wazuh decoders, rules, and simulated security events.
- **Network Monitoring:** Zeek protocol telemetry and anomaly analysis.
- **Deception Technology:** Cowrie SSH honeypot deployment and session observation.
- **Telemetry Engineering:** Structured event collection and centralized logging.
- **Security Visualization:** Grafana dashboards and Loki-based log exploration.
- **Threat Hunting:** Examination of authentication activity, network behavior, and suspicious interactions.

The goal is to build a reproducible defensive monitoring environment that transforms simulated security activity and honeypot interactions into structured, searchable, and actionable telemetry.

---

## 👤 Author

**Brandon Lawrence Gregg**  
GitHub: [BlueSilverX4](https://github.com/BlueSilverX4)

*Defensive Cybersecurity Engineering & Infrastructure Lab*
