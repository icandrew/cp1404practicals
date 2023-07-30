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
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["Jake", "Micaela", "Elaine", "Isabel"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.root.ids.labels_box.clear_widgets()
        for name in self.names:
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            self.root.ids.labels_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = f"{name}"

    def clear_all(self):
        self.root.ids.labels_box.clear_widgets()


DynamicWidgetsApp().run()
