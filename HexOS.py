import os
from configparser import ConfigParser

from appdirs import user_data_dir

import HexOSLibs

sysConfig = ConfigParser()
sysConfig.read("sysConfig.ini")

os.environ['KIVY_HOME'] = user_data_dir(sysConfig["main"]["name"])
os.environ['KIVY_CONFIG_FILE'] = os.path.join(os.getcwd(), "kivyConfig.ini")
os.environ[str(sysConfig["main"]["name"]) + '_CONFIG'] = str(sysConfig.__dict__)
os.chdir(user_data_dir(sysConfig["main"]["name"]))

HexOSLibs.setup_os()
HexOSLibs.start_os()

