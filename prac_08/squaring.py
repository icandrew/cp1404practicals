from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 150)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root


SquareNumberApp().run()
