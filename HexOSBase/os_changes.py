import os

from kivy import Logger

from HexOSBase.functions import copytree
from HexOSBase import globals


def copy():
    Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": Starting OS copy")

    copytree(os.path.join(globals.baseSysPath, globals.baseSysConfig.get("main", "name") + "Files"),
             globals.HexOSPath)

    Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": Finished OS copy")


def try_update():
    if open(os.path.join(globals.baseSysPath,
                         globals.baseSysConfig.get("main", "name") + "Files", "OSVer"), "r").read() \
            != open(os.path.join(globals.HexOSPath, "OSVer"), "r").read():
        print("fe")
        copy()


def install():
    copy()


__all__ = ["try_update", "install"]
