from kivy.app import App
from kivy.lang import Builder

class BoxLayout(App):
    def build(self):
        self.root = Builder.load_file('box_layout.kv')
        return self.root


    def handle_greet(self):
        print("greet")

if __name__ == '__main__':
    BoxLayout().run()