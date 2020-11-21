from kivy.app import App

from HexOS.window import Window
from sys_config import sysConfig


class HexOS(App):
    title = sysConfig.get("main", "name")

    def build(self):
        return Window()
