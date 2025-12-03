# trade_producer.py

import random
import logging
import uuid
from typing import List
from config import TRADE_SYMBOLS, TRADE_SIDES, APP_LOG_PATH
from database import insert_trade

# Configure logging
logging.basicConfig(
    filename=APP_LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s [PRODUCER] %(levelname)s: %(message)s",
)

def generate_trade() -> tuple:
    """Generate a single fake trade."""
    trade_id = str(uuid.uuid4())
    symbol = random.choice(TRADE_SYMBOLS)
    side = random.choice(TRADE_SIDES)
    quantity = random.randint(1, 10_000)

    # random realistic price per share
    price = round(random.uniform(10, 500), 2)
    amount = round(quantity * price, 2)

    # status is always NEW for now
    status = "NEW"

    return (trade_id, symbol, side, quantity, price, amount, status)

def produce_trades(count: int = 100):
    """Create and persist a batch of trades."""
    logging.info(f"Starting to produce {count} trades.")
    for _ in range(count):
        trade = generate_trade()
        try:
            insert_trade(trade)
            logging.info(
                f"Inserted trade: id={trade[0]} symbol={trade[1]} side={trade[2]} "
                f"qty={trade[3]} price={trade[4]} amount={trade[5]}"
            )
        except Exception as e:
            logging.error(f"Failed to insert trade {trade[0]}: {e}")
    logging.info("Finished producing trades.")
