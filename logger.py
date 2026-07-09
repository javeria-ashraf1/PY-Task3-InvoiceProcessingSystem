import logging
import os
from config import LOG_FOLDER, LOG_FILE

os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def write_log(message):
    logging.info(message)