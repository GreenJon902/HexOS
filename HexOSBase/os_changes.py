import os
import time
from threading import Thread

from kivy import Logger
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar

from HexOSBase.functions import copytree
from HexOSBase import globals

from HexOSBase.tmpdir import make_tmp_dir


def _copy(bar, src):
    time.sleep(globals.baseSysConfig.get("os_changes", "wait_before"))

    Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": Starting OS copy")

    copytree(src, globals.HexOSPath, bar)

    Logger.info(globals.baseSysConfig.get("main", "parent_name") + ": Finished OS copy")

    time.sleep(globals.baseSysConfig.get("os_changes", "wait_after"))

    bar.parent.parent.parent.dismiss()


def copy(bar):
    Thread(target=_copy, args=(bar,)).start()


def try_update_for_testing():
    bar = window("update")
    if open(os.path.join(globals.baseSysPath,
                         globals.baseSysConfig.get("main", "name") + "Files", "OSVer"), "r").read() \
            != open(os.path.join(globals.HexOSPath, "OSVer"), "r").read():
        copy(bar, os.path.join(globals.baseSysPath, globals.baseSysConfig.get("main", "name") + "Files"))


def install():
    bar = window("install")
    tmpDir = make_tmp_dir("install")
    copy(bar, )


def window(doing):
    if doing == "update":
        doing = "updat"
    doing = doing.title()

    bar = ProgressBar(max=len(list(os.walk(os.path.join(globals.baseSysPath, globals.baseSysConfig.get("main", "name")
                                                        + "Files")))))

    popup = Popup(title=doing + "ing HexOS",
                  content=bar,
                  size_hint=(globals.baseSysConfig.get("os_changes", "size_hint_x"),
                             globals.baseSysConfig.get("os_changes", "size_hint_y")),
                  auto_dismiss=False)

    popup.open()

    return bar


__all__ = ["try_update_for_testing", "install"]
