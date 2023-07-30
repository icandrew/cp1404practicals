from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometerApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (640, 480)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKilometerApp().run()
