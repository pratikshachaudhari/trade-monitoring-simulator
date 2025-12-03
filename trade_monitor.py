# trade_monitor.py

import logging
from typing import List
from config import APP_LOG_PATH, ALERT_LOG_PATH, MAX_TRADE_AMOUNT, MIN_TRADE_AMOUNT
from database import fetch_recent_trades

# App log
logging.basicConfig(
    filename=APP_LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s [MONITOR] %(levelname)s: %(message)s",
)

# Separate logger for alerts
alert_logger = logging.getLogger("alerts")
alert_handler = logging.FileHandler(ALERT_LOG_PATH)
alert_formatter = logging.Formatter("%(asctime)s [ALERT] %(levelname)s: %(message)s")
alert_handler.setFormatter(alert_formatter)
alert_logger.addHandler(alert_handler)
alert_logger.setLevel(logging.WARNING)

def run_basic_checks():
    """Run simple anomaly checks on recent trades."""
    trades = fetch_recent_trades(limit=100)

    total_trades = len(trades)
    logging.info(f"Running checks on {total_trades} recent trades.")

    for row in trades:
        trade_id = row["trade_id"]
        symbol = row["symbol"]
        side = row["side"]
        amount = row["amount"]
        quantity = row["quantity"]

        # Check 1: extremely large trades
        if amount > MAX_TRADE_AMOUNT:
            msg = (
                f"High amount trade detected: trade_id={trade_id}, "
                f"symbol={symbol}, side={side}, amount={amount}"
            )
            alert_logger.warning(msg)

        # Check 2: suspiciously low trades
        if amount < MIN_TRADE_AMOUNT:
            msg = (
                f"Unusually small trade detected: trade_id={trade_id}, "
                f"symbol={symbol}, side={side}, amount={amount}"
            )
            alert_logger.warning(msg)

        # Check 3: zero or negative quantity
        if quantity <= 0:
            msg = (
                f"Invalid quantity detected: trade_id={trade_id}, "
                f"symbol={symbol}, qty={quantity}"
            )
            alert_logger.error(msg)

    logging.info("Monitoring checks completed.")
