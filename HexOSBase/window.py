from io import BytesIO

from PIL import ImageGrab, Image as PILImage
from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window as CoreWindow
from kivy.uix.floatlayout import FloatLayout

from HexOSBase.baseSysConfigurator import BaseSysConfigurator
from globals import baseSysConfig


class Window(FloatLayout):
    screenShotClock = None

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        CoreWindow.bind(left=self.on_pos, top=self.on_pos)
        CoreWindow.bind(on_hide=self.take_screenshot_clock_start, on_show=self.take_screenshot_clock_stop)

        Clock.schedule_once(self.take_whole_screen_screenshot, 0)
        Clock.schedule_once(self.je, 2)
        Clock.schedule_interval(self.take_not_window_screenshot, baseSysConfig.get("background_image",
                                                                                   "open_refresh_rate"))

        Logger.info(baseSysConfig.get("main", "parent_name") + ": Window class has initiated")

        if baseSysConfig.get("background_image", "see_through") == "True":
            Logger.info(baseSysConfig.get("main", "parent_name") + ": Window was created see through")

        else:
            Logger.info(baseSysConfig.get("main", "parent_name") + ": Window was created not see through")

    def on_parent(self, *args):
        if baseSysConfig.get("background_image", "see_through"):
            self.ids["ParentScreenImage"].opacity = 1
            self.ids["SeeThroughButton"].state = "down"
            
        else:
            self.ids["ParentScreenImage"].opacity = 0
            self.ids["SeeThroughButton"].state = "normal"


    def on_pos(self, *args):
        if baseSysConfig.get("background_image", "see_through"):
            self.ids["ParentScreenImage"].pos = 0 - CoreWindow.left, \
                                                (CoreWindow.top + CoreWindow.height) - \
                                                self.ids["ParentScreenImage"].size[1]

    def take_whole_screen_screenshot(self, *args):
        if baseSysConfig.get("background_image", "see_through"):
            img = ImageGrab.grab()
            data = BytesIO()
            img.save(data, format="png")
            data.seek(0)
            img = CoreImage(BytesIO(data.read()), ext='png')

            self.ids["ParentScreenImage"].texture = img.texture
            self.ids["ParentScreenImage"].size = img.size
            self.ids["ParentScreenImage"].pos = 0 - CoreWindow.left, 0 - CoreWindow.top

    def take_not_window_screenshot(self, shouldWholeWindowIfNone=False, *args):
        if baseSysConfig.get("background_image", "see_through"):
            img = ImageGrab.grab()

            try:
                im = CoreImage(self.ids["ParentScreenImage"].texture)

            except Exception:
                Logger.warning(baseSysConfig.get("main", "parent_name") +
                               ": Window background image does not have a texture")

                if shouldWholeWindowIfNone:
                    self.minimize_screenshot()

                return

            data = BytesIO()
            im.save(data, fmt="png")
            data.seek(0)
            im = PILImage.open(data)

            wx, wy, ww, wh = CoreWindow.left, CoreWindow.top, CoreWindow.width, CoreWindow.height
            remAmount = baseSysConfig.get("background_image", "crop_distance")
            remAmountTop = baseSysConfig.get("background_image", "crop_distance_top")
            x, y, x2, y2 = wx - remAmount, wy - remAmountTop, wx + ww + remAmount, wy + wh + remAmount
            im = im.crop((x, y, x2, y2))

            img.paste(im, (x, y))

            data = BytesIO()
            img.save(data, format="png")
            data.seek(0)
            img = CoreImage(BytesIO(data.read()), ext='png')

            self.ids["ParentScreenImage"].texture = img.texture




    def take_screenshot_clock_start(self, *args):
        self.screenShotClock = Clock.schedule_interval(self.take_whole_screen_screenshot,
                                                       baseSysConfig.get("background_image", "minimized_refresh_rate"))

    def take_screenshot_clock_stop(self, *args):
        if self.screenShotClock is not None:
            self.screenShotClock.cancel()
            self.screenShotClock = None

    def see_through_flip(self, active):

        if active == "normal":
            active = False
            Logger.info(baseSysConfig.get("main", "parent_name") + ": Window is now not see through")
        else:
            active = True
            Logger.info(baseSysConfig.get("main", "parent_name") + ": Window is now see through")



        baseSysConfig.set("background_image", "see_through", str(active))

        self.ids["StrongRefreshButton"].disabled = not active
        self.ids["WeakRefreshButton"].disabled = not active

        if active:
            self.take_not_window_screenshot(shouldWholeWindowIfNone=True)
            self.on_pos()

            a = Animation(opacity=1, duration=baseSysConfig.get("background_image", "fade_time"))

            Clock.schedule_once(lambda *args: a.start(self.ids["ParentScreenImage"]),
                                baseSysConfig.get("background_image", "fade_wait"))

        else:
            a = Animation(opacity=0, duration=baseSysConfig.get("background_image", "fade_time"))

            Clock.schedule_once(lambda *args: a.start(self.ids["ParentScreenImage"]),
                                baseSysConfig.get("background_image", "fade_wait"))

    def minimize_screenshot(self, *args):
        CoreWindow.hide()
        Clock.schedule_once(lambda *args: self.take_whole_screen_screenshot(), 0.1)
        Clock.schedule_once(lambda *args: CoreWindow.show(), 0.2)
