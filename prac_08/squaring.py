"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Started 20/07/2025
"""

from kivy.app import App
from kivy.lang import Builder

class SquareApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        self.root = Builder.load_file("squaring.kv")
        return self.root


    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_number.text = str(result)
        except ValueError:
            self.root.ids.output_number.text = "Invalid input"


if __name__ == '__main__':
    SquareApp().run()