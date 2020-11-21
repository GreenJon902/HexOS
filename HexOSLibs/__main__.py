import os
import sys

print(sys.path, os.getcwd())
from kivy.app import App

from HexOSLibs.window import Window


class HexOS(App):
    def build(self):
        return Window()
