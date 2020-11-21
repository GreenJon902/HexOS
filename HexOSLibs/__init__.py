import os


def setup_os():
    from kivy.config import Config
    Config.read(os.environ['KIVY_CONFIG_FILE'])

    for i in os.listdir("logs"):
        if os.path.isfile(os.path.join(Config.get("kivy", "log_dir"), i)) and 'kivy' in i:
            os.remove(os.path.join(Config.get("kivy", "log_dir"), i))


def start_os():
    from HexOSLibs.__main__ import HexOS

    HexOS().run()


__all__ = ["setup_os",
           "start_os"]
