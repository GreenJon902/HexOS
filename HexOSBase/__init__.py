import os

from kivy.clock import Clock

from HexOSBase import globals, os_changes


def setup_os():
    from kivy.config import Config
    Config.read(os.environ['KIVY_CONFIG_FILE'])

    for i in os.listdir("logs"):
        if os.path.isfile(os.path.join(Config.get("kivy", "log_dir"), i)) and 'kivy' in i:
            os.remove(os.path.join(Config.get("kivy", "log_dir"), i))

    from kivy.logger import Logger

    Logger.info(globals.baseSysConfig.get("main", "name") + ": " + globals.baseSysConfig.get("main", "parent_name") +
                "'s logger has been setup")

    from kivy.lang.builder import Builder
    Builder.load_file(os.path.join(globals.baseSysPath, "HexOSBase/data/kv_files/window.kv"))

    Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": window.kv has loaded")

    if not os.path.exists(globals.HexOSPath):
        Clock.schedule_once(lambda *args: os_changes.install(), 0)

    if globals.baseSysConfig.get("HexOS", "update_on_start"):
        Clock.schedule_once(lambda *args: os_changes.try_update(), 0)


def start_os():
    from HexOSBase.__main__ import HexOSBase

    from kivy.logger import Logger

    Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": " + globals.baseSysConfig.get("main",
                                                                                                    "parent_name") + " is starting")

    HexOSBase().run()


__all__ = ["setup_os",
           "start_os"]
