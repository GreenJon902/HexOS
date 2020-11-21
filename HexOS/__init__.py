import os

from sys_config import sysConfig


def setup_os():
    from kivy.config import Config
    Config.read(os.environ['KIVY_CONFIG_FILE'])

    for i in os.listdir("logs"):
        if os.path.isfile(os.path.join(Config.get("kivy", "log_dir"), i)) and 'kivy' in i:
            os.remove(os.path.join(Config.get("kivy", "log_dir"), i))

    from kivy.logger import Logger

    Logger.info(sysConfig.get("main", "name") + ": HexOS's logger has been setup")


def start_os():
    from HexOS.__main__ import HexOS

    from kivy.logger import Logger

    Logger.info(sysConfig.get("main", "name") + ": HexOS is starting")

    HexOS().run()


__all__ = ["setup_os",
           "start_os"]
