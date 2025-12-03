# Trade Monitoring & Alerting Simulator  

---

Overview
This project simulates a **mini trading platform** and demonstrates how an Application Support Engineer monitors, validates, and investigates live trade data.

It includes:
- automatic trade generation  
- database storage  
- anomaly detection  
- alerting  
- structured logging  
- monitoring logic  

---
Project Features

Trade Producer  
Generates fake trades (BUY/SELL) with:
- symbol, side  
- price, quantity  
- amount  
- status  
- timestamp  

Trades are written to:
- SQLite database (`trades.db`)  
- app log (`app.log`)

---

Monitoring System  
Checks most recent trades for:
- unusually large amounts  
- suspiciously small amounts  
- invalid quantities  
- malformed entries  

Alerts are written to `alerts.log`.

---

Database  
Uses SQLite (built into Python).  
Table: **trades**

Fields:
- trade_id  
- symbol  
- side  
- quantity  
- price  
- amount  
- status  
- created_at  

---

Architecture Diagram

```
Frontend (Trade Generator)
        |
        v
SQLite Database <----> Monitoring Script
        |
        v
 Alert Logs (alerts.log)
        |
        v
 App Logs (app.log)
```

---

File Structure

```
trade-monitoring-simulator/
│
├── main.py            # Run full project
├── config.py          # Settings / thresholds
├── database.py        # DB functions + table creation
├── trade_producer.py  # Generates fake trades
├── trade_monitor.py   # Detects anomalies
│
├── logs/
│   ├── app.log
│   └── alerts.log
│
└── data/
    └── trades.db
```

---

How to Run

Clone this repository
    git clone https://github.com/your-username/trade-monitoring-simulator.git
    cd trade-monitoring-simulator
Run the project
    python main.py
Check outputs
- `logs/app.log` → trade activity  
- `logs/alerts.log` → alerts  
- `data/trades.db` → use DB Browser for SQLite to view data  

---

Sample Alerts

```
2025-01-10 [ALERT] WARNING: High amount trade detected: trade_id=..., symbol=AAPL, amount=1250000.00
2025-01-10 [ALERT] ERROR: Invalid quantity detected: trade_id=..., qty=0
```

---

Future Enhancements
You can expand the project with:
- API latency simulation  
- failed message retries  
- trade replay logic  
- email/SMS alerting  
- dashboard (Streamlit/Power BI)  
- cron-based intraday checks  
- config-based deployment validations  


Author
Pratiksha Chaudhari  
Application Support / SRE Support Engineer  

LinkedIn: *your link*  
GitHub: *your link*
