# config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database path
DB_PATH = os.path.join(BASE_DIR, "data", "trades.db")

# Log files
APP_LOG_PATH = os.path.join(BASE_DIR, "logs", "app.log")
ALERT_LOG_PATH = os.path.join(BASE_DIR, "logs", "alerts.log")

# Trade settings
TRADE_SYMBOLS = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN"]
TRADE_SIDES = ["BUY", "SELL"]

# Monitoring thresholds
MAX_TRADE_AMOUNT = 1_000_000      # alert for very large trades
MIN_TRADE_AMOUNT = 10             # alert for suspiciously small trades
