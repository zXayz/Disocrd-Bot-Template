from __future__ import annotations

import sys
import logging
import logging.config

from setup import BaseBot
from core.config import BOT_TOKEN
from core.logger import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("bot")

def log_uncaught_exceptions(exctype, value, tb):
    logging.error("Uncaught exception: ", exc_info=(exctype, value, tb))

sys.excepthook = log_uncaught_exceptions

bot = BaseBot()

if __name__ == "__main__":
    bot.run(BOT_TOKEN, root_logger=True)
    
    