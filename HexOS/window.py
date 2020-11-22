from io import BytesIO

from PIL import ImageGrab, Image as PILImage
from kivy import Logger
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window as CoreWindow
from kivy.uix.floatlayout import FloatLayout

from globals import sysConfig


class Window(FloatLayout):
    screenShotClock = None

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        CoreWindow.bind(left=self.on_pos, top=self.on_pos)
        CoreWindow.bind(on_show=self.take_screenshot_clock_stop)
        CoreWindow.bind(on_hide=self.take_screenshot_clock_start)


        Clock.schedule_once(self.take_whole_screen_screenshot, 0)
        Clock.schedule_interval(self.take_not_window_screenshot, 10)

    def on_pos(self, *args):
        self.ids["parentScreenImage"].pos = 0 - CoreWindow.left, \
                                            (CoreWindow.top + CoreWindow.height) - self.ids["parentScreenImage"].size[1]

    def take_whole_screen_screenshot(self, *args):
        img = ImageGrab.grab()
        data = BytesIO()
        img.save(data, format="png")
        data.seek(0)
        img = CoreImage(BytesIO(data.read()), ext='png')

        self.ids["parentScreenImage"].texture = img.texture
        self.ids["parentScreenImage"].size = img.size
        self.ids["parentScreenImage"].pos = 0 - CoreWindow.left, 0 - CoreWindow.top

    def take_not_window_screenshot(self, *args):
        img = ImageGrab.grab()

        try:
            im = CoreImage(self.ids["parentScreenImage"].texture)

        except Exception:
            Logger.warning(sysConfig.get("main", "parent_name") + ": Window background image does not have a texture")
            return

        data = BytesIO()
        im.save(data, fmt="png")
        data.seek(0)
        im = PILImage.open(data)

        wx, wy, ww, wh = CoreWindow.left, CoreWindow.top, CoreWindow.width, CoreWindow.height
        remAmount = int(sysConfig.get("background_image", "crop_distance"))
        remAmountTop = int(sysConfig.get("background_image", "crop_distance_top"))
        x, y, x2, y2 = wx - remAmount, wy - remAmountTop, wx + ww + remAmount, wy + wh + remAmount
        im = im.crop((x, y, x2, y2))

        img.paste(im, (x, y))

        data = BytesIO()
        img.save(data, format="png")
        data.seek(0)
        img = CoreImage(BytesIO(data.read()), ext='png')

        self.ids["parentScreenImage"].texture = img.texture




    def take_screenshot_clock_start(self, *args):
        self.screenShotClock = Clock.schedule_interval(self.take_screenshot, 1)

    def take_screenshot_clock_stop(self, *args):
        if self.screenShotClock is not None:
            self.screenShotClock.cancel()
            self.screenShotClock = None
