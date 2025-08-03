from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

@app.route('/f/<celsius>')
def convert(celsius):
    """Convert Celsius from URL to Fahrenheit."""
    try:
        celsius_value = float(celsius)
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        return f"{celsius_value:.2f}°C = {fahrenheit_value:.2f}°F"
    except ValueError:
        return "Invalid input. Please enter a number like /f/36.5"

if __name__ == '__main__':
    app.run()
