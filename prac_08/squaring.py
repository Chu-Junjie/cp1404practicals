from kivy.app import App
from kivy.lang import Builder

class SquareApp(App):
    def build(self):
        self.root = Builder.load_file("squaring.kv")
        return self.root


    def handle_calculate(self):
        try:
            value = float(self.root.ids.input_number.text)
            result = value ** 2
            self.root.ids.output_number.text = str(result)
        except ValueError:
            self.root.ids.output_number.text = "Invalid input"


if __name__ == '__main__':
    SquareApp().run()