import os
import shutil

import globals


def copytree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d)
        else:
            shutil.copy2(s, d)


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

    if globals.baseSysConfig.get("HexOS", "reinstall_every_time"):
        Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": Starting OS copy")

        copytree(os.path.join(globals.baseSysPath, globals.baseSysConfig.get("main", "name") + "Files"),
                 globals.HexOSPath)

        Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": Finished OS copy")


def start_os():
    from HexOSBase.__main__ import HexOS

    from kivy.logger import Logger

    Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": " + globals.baseSysConfig.get("main",
                                                                                                    "parent_name") + " is starting")

    HexOS().run()


__all__ = ["setup_os",
           "start_os"]
