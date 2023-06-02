from configparser import ConfigParser
from Common.handle_path import CONF_DIR
import os
class Config(ConfigParser):
    def __init__(self,file_name,encoding="utf-8"):
        super().__init__()
        self.read(file_name,encoding="utf-8")

cfg = Config(file_name=os.path.join(CONF_DIR,"config.ini"))

# print(cfg.get("musen","age"))
