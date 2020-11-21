import os


def setup_app():
    from kivy.config import Config
    Config.read("kivyConfig.ini")
    os.environ['KIVY_CONFIG'] = str(Config.__dict__)


def start_app():
    import HexOSLibs.__main__
