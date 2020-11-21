from kivy.app import App

from HexOSLibs.window import Window
from sys_config import sysConfig


class HexOS(App):
    title = sysConfig.get("main", "name")

    def build(self):
        return Window()
