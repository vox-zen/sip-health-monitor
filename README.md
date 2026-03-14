# SIP Health Monitor

SIP Health Monitor is a simple tool to monitor the availability and health of SIP trunks and endpoints.

It helps VoIP engineers detect issues such as:

- SIP trunk downtime
- connectivity problems
- high latency
- unreachable SIP endpoints

The tool periodically sends SIP OPTIONS requests or network checks to verify trunk status.

---

# Features

- monitor SIP trunk availability
- detect unreachable SIP endpoints
- latency checks
- simple JSON configuration
- CLI monitoring output

---

# Example Output

Trunk: provider1
-
Status: OK
-
Latency: 24ms
-
Trunk: provider2
-
Status: DOWN
-

---

# Use Cases

- VoIP infrastructure monitoring
- call center SIP trunk monitoring
- telecom NOC monitoring
- VoIP system health checks

---

# Project Structure

monitor/
main monitoring script

scripts/
helper scripts

docs/
architecture documentation

---

# Example Configuration

config.json

```bash
{
"trunks": [
{
"name": "provider1",
"host": "sip.provider1.com",
"port": 5060
},
{
"name": "provider2",
"host": "sip.provider2.com",
"port": 5060
}
]
}
```

---

# Running Monitor

python monitor/sip_monitor.py

---

# Roadmap

- SIP OPTIONS ping
- RTP health monitoring
- alert notifications
- Prometheus metrics
- Grafana integration

---

# License

MIT
