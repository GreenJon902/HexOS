from kivy.app import App

from HexOS.window import Window
from globals import sysConfig


class HexOS(App):
    title = sysConfig.get("main", "name")

    def build(self):
        return Window()

    def on_stop(self):
        print("Fe")
