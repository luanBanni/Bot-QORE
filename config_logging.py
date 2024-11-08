import logging
from config import LOG_DIR


def config_logging():
  logging.basicConfig(filename=LOG_DIR, level=logging.INFO,
   format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
  )