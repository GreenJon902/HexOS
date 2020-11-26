import os

from kivy.app import App
from kivy.core.window import Window as CoreWindow

from HexOSBase.window import Window
import globals


class HexOS(App):
    title = globals.baseSysConfig.get("main", "name")

    def build(self):
        CoreWindow.bind(on_request_close=self.on_close)

        return Window()


    def on_close(self, *args):
        globals.baseSysConfig.write(open(os.path.join(globals.baseSysPath, "HexOSBase/data/config_files/base_sys_config.ini"), "w"))


__all__ = ["HexOS"]
