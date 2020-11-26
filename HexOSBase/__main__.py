import os

from kivy.app import App
from kivy.core.window import Window as CoreWindow

from HexOSBase.window import Window
from globals import baseSysConfig, path


class HexOS(App):
    title = baseSysConfig.get("main", "name")

    def build(self):
        CoreWindow.bind(on_request_close=self.on_close)

        return Window()


    def on_close(self, *args):
        baseSysConfig.write(open(os.path.join(path, "HexOSBase/data/config_files/base_sys_config.ini"), "w"))
