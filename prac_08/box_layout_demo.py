from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.root = Builder.load_file('box_layout.kv')
        return self.root


    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello"


if __name__ == '__main__':
    BoxLayoutDemo().run()