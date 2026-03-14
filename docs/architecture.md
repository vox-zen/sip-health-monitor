# SIP Health Monitor Architecture

SIP Health Monitor checks the connectivity of SIP trunks and endpoints.

Monitoring Flow:

Monitor Script
↓
Load trunk configuration
↓
Check network connectivity to SIP host
↓
Measure latency
↓
Report status

Possible extensions:

- SIP OPTIONS monitoring
- RTP stream checks
- Prometheus exporter
- Alert notifications
