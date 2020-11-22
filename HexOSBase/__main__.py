from kivy.app import App

from HexOSBase.window import Window
from globals import sysConfig


class HexOS(App):
    title = sysConfig.get("main", "name")

    def build(self):
        return Window()
