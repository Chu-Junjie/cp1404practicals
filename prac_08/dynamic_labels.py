from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Main application class for dynamically adding labels."""
    def build(self):
        self.root = Builder.load_file("dynamic_labels.kv")

        self.root.ids.main.add_widget(Label(text="Hello"))
        self.root.ids.main.add_widget(Label(text="World"))
        self.root.ids.main.add_widget(Label(text="!"))
        return self.root

if __name__ == '__main__':
    DynamicLabelsApp().run()
