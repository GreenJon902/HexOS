import os

from kivy.app import App
from kivy.core.window import Window as CoreWindow

from HexOSBase.window import Window
from globals import sysConfig, path


class HexOS(App):
    title = sysConfig.get("main", "name")

    def build(self):
        CoreWindow.bind(on_request_close=self.on_close)

        return Window()


    def on_close(self, *args):
        print(sysConfig.get("background_image", "see_through"))
        sysConfig.write(open(os.path.join(path, "HexOSBase/data/config_files/sys_config.ini"), "w"))
