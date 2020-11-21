import os
import sys
from appdirs import user_data_dir

import HexOS
import globals


globals.path = os.getcwd()

sys.path.append(os.getcwd())

os.environ['KIVY_HOME'] = user_data_dir(globals.sysConfig["main"]["name"])
os.environ['KIVY_CONFIG_FILE'] = os.path.join(os.getcwd(), "kivyConfig.ini")
os.chdir(user_data_dir(globals.sysConfig["main"]["name"]))

HexOS.setup_os()
HexOS.start_os()
