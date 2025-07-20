from kivy.app import App
from kivy.lang import Builder

class SquareApp(App):
    def build(self):
        self.root = Builder.load_file("squaring.kv")
        return self.root


    def handle_calculate(self):
        print("Square")

if __name__ == '__main__':
    SquareApp().run()