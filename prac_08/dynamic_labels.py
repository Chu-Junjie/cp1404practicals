from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        self.root = Builder.load_file("dynamic_labels.kv")

        return self.root

if __name__ == '__main__':
    DynamicLabelsApp().run()
