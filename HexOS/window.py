from io import BytesIO

from PIL import ImageGrab
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window as CoreWindow
from kivy.uix.floatlayout import FloatLayout


class Window(FloatLayout):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        CoreWindow.bind(left=self.on_pos, top=self.on_pos)

    def on_pos(self, _, pos):
        self.ids["parentScreenImage"].pos = 0 - CoreWindow.left, \
                                            (CoreWindow.top + CoreWindow.height) - self.ids["parentScreenImage"].size[1]

    def on_size(self, _, size):
        img = ImageGrab.grab()
        data = BytesIO()
        img.save(data, format='png')
        data.seek(0)
        img = CoreImage(BytesIO(data.read()), ext='png')

        self.ids["parentScreenImage"].texture = img.texture
        self.ids["parentScreenImage"].size = img.size
        self.ids["parentScreenImage"].pos = 0 - CoreWindow.left, 0 - CoreWindow.top
