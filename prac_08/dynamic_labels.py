"""
CP1404 Practical 08 - Dynamic Labels
Estimated time to complete 120min
Time to complete - 
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root


DynamicWidgetsApp().run()
