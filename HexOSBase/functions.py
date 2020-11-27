import os
import shutil


def copytree(src, dst, bar):

    if not os.path.exists(dst):
        os.mkdir(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, bar)
        else:
            shutil.copy2(s, d)

        bar.value = bar.value + 1


__all__ = ["copytree"]
