import os
import sys
from appdirs import user_data_dir

import HexOSBase
import globals

if __name__ == '__main__':
    globals.baseSysPath = os.getcwd()

    sys.path.append(os.getcwd())

    os.environ['KIVY_HOME'] = user_data_dir(globals.baseSysConfig.get("main", "name"))
    os.environ['KIVY_CONFIG_FILE'] = os.path.join(os.getcwd(), "HexOSBase/data/config_files/kivy_config.ini")
    os.chdir(user_data_dir(globals.baseSysConfig.get("main", "name")))

    globals.HexOSPath = os.path.join(user_data_dir(globals.baseSysConfig.get("main", "name")),
                                     globals.baseSysConfig.get("HexOS", "folder_name"))

    HexOSBase.setup_os()
    HexOSBase.start_os()

__all__ = []
