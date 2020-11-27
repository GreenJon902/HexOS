import os
import shutil


def copytree(src, dst):

    if not os.path.exists(dst):
        os.mkdir(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d)
            print(item, 1)
        else:
            print(item, 2)
            shutil.copy2(s, d)


__all__ = ["copytree"]
