import os
import shutil

from HexOSBase import globals


def make_tmp_dir(doing):
    if not os.path.exists(os.path.join(globals.userDataDir, "tmp")):
        os.mkdir(os.path.join(globals.userDataDir, "tmp"))

    path = os.path.join(globals.userDataDir, "tmp", doing)
    os.mkdir(path)

    return path


def clear_tmp_dir():
    folder = os.path.exists(os.path.join(globals.userDataDir, "tmp"))

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:
            from kivy import Logger
            Logger.exception("Failed to clear tmp folder - " + str(e))


__all__ = ["clear_tmp_dir", "make_tmp_dir"]
