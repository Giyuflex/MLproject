import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Complete path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s"
)

