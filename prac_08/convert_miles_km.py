from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.609344


class ConvertMilesToKilometerApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    user_input = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (640, 320)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) * MILES_TO_KILOMETERS  # 1mile = 1.609344km
            self.root.ids.output_label.text = f"{result:.5f}"
        except ValueError:
            pass

    def handle_update(self, text, change):
        try:
            current_miles = float(text)
            updated_miles = current_miles + change
            self.user_input = str(updated_miles)
            self.root.ids.user_input.text = str(updated_miles)
        except ValueError:
            pass

    def convert_str_to_int(self, value):
        try:
            value = float(self.root.ids.user_input.text)
        except ValueError:
            value = 0.0
        return value


ConvertMilesToKilometerApp().run()
