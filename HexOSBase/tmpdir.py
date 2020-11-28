import os
import shutil

from kivy import Logger

from HexOSBase import globals


def make_tmp_dir(doing):
    try:
        if not os.path.exists(os.path.join(globals.userDataDir, "tmp")):
            os.mkdir(os.path.join(globals.userDataDir, "tmp"))

        path = os.path.join(globals.userDataDir, "tmp", doing)
        os.mkdir(path)

        Logger.info("HexOSBase: tmp dir " + doing + " created")

    except FileExistsError:

        Logger.error("HexOSBase: Failed to create tmp folder named " + doing + ", creating a different one")
        path = make_tmp_dir(doing + str(2))

    return path


def clear_tmp_dir():
    try:
        folder = os.path.exists(os.path.join(globals.userDataDir, "tmp"))

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        Logger.info("HexOSBase: tmp dir cleared")

    except Exception as e:
        Logger.error("HexOSBase: Failed to clear tmp folder - " + str(e))


__all__ = ["clear_tmp_dir", "make_tmp_dir"]
