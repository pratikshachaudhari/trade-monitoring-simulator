# main.py

import os
from database import init_db
from trade_producer import produce_trades
from trade_monitor import run_basic_checks
from config import APP_LOG_PATH, ALERT_LOG_PATH, DB_PATH

def ensure_directories():
    """Make sure data/ and logs/ exist."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(base_dir, "logs")
    data_dir = os.path.join(base_dir, "data")

    os.makedirs(logs_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

def main():
    ensure_directories()

    print("Initialising database...")
    init_db()
    print(f"Database ready at: {DB_PATH}")

    print("Producing trades...")
    produce_trades(count=100)
    print("Trades generated.")

    print("Running monitoring checks...")
    run_basic_checks()
    print("Monitoring completed.")

    print("\nCheck these files:")
    print(f"- App log: {APP_LOG_PATH}")
    print(f"- Alert log: {ALERT_LOG_PATH}")
    print("You can also open the SQLite DB (trades.db) using any DB browser.")

if __name__ == "__main__":
    main()
