from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """Main application class for the Miles to Kilometres converter"""
    output_text = StringProperty()
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = "0.0"
        return self.root

    def convert(self):
        """Convert miles to km when 'Convert' button pressed"""
        miles = self.get_miles()
        km = miles * MILES_TO_KM
        self.output_text = str(km)

    def handle_increment(self, change):
        """Handle Up/Down buttons"""
        miles = self.get_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.convert()

    def get_miles(self):
        """Get float value from input field, or 0 if invalid"""
        try:
            miles_text = self.root.ids.input_miles.text
            return float(miles_text)
        except ValueError:
            return 0.0


if __name__ == '__main__':
    MilesConverterApp().run()