import os

from globals import path, sysConfig


def setup_os():
    from kivy.config import Config
    Config.read(os.environ['KIVY_CONFIG_FILE'])

    for i in os.listdir("logs"):
        if os.path.isfile(os.path.join(Config.get("kivy", "log_dir"), i)) and 'kivy' in i:
            os.remove(os.path.join(Config.get("kivy", "log_dir"), i))

    from kivy.logger import Logger

    Logger.info(sysConfig.get("main", "name") + ": HexOSBase's logger has been setup")


    from kivy.lang.builder import Builder
    Builder.load_file(os.path.join(path, "HexOSBase/data/kv_files/window.kv"))

    Logger.info(sysConfig.get("main", "parent_name") + ": window.kv has loaded")


def start_os():
    from HexOSBase.__main__ import HexOS

    from kivy.logger import Logger

    Logger.info(sysConfig.get("main", "parent_name") + ": " + sysConfig.get("main", "parent_name") + " is starting")

    HexOS().run()


__all__ = ["setup_os",
           "start_os"]
