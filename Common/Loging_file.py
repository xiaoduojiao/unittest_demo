import logging
from logging.handlers import TimedRotatingFileHandler
# from handle_path import LOG_DIR
# from config import cfg
from Common.handle_path import LOG_DIR
from Common.config  import cfg
import os

class Handlog:
    @staticmethod
    def create_logger():
        log = logging.getLogger("TC")
        log.setLevel(cfg.get("logging","lelvel"))

        fh = TimedRotatingFileHandler(filename=os.path.join(LOG_DIR,cfg.get('logging','log_name')), when="h", interval=1, backupCount=7, encoding="utf-8")
        fh.setLevel(cfg.get("logging","fh_level"))
        log.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(cfg.get("logging","sh_level"))
        log.addHandler(sh)

        formatter = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        mate = logging.Formatter(formatter)
        fh.setFormatter(mate)
        sh.setFormatter(mate)

        return log

log = Handlog().create_logger()
