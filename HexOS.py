import os
import sys
from appdirs import user_data_dir

import HexOS
from globals import sysConfig

sys.path.append(os.getcwd())

os.environ['KIVY_HOME'] = user_data_dir(sysConfig["main"]["name"])
os.environ['KIVY_CONFIG_FILE'] = os.path.join(os.getcwd(), "kivyConfig.ini")
os.chdir(user_data_dir(sysConfig["main"]["name"]))

HexOS.setup_os()
HexOS.start_os()
