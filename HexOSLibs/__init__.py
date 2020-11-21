import os


def setup_os():
    from kivy.config import Config
    Config.read(os.environ['KIVY_CONFIG_FILE'])
    os.environ['KIVY_CONFIG'] = str(Config.__dict__)

    for i in os.listdir("logs"):
        if os.path.isfile(os.path.join(Config.get("kivy", "log_dir"), i)) and 'kivy' in i:
            os.remove(os.path.join(Config.get("kivy", "log_dir"), i))

def start_os():
    import HexOSLibs.__main__


__all__ = ["setup_os",
           "start_os"]
