from flask import Flask, request

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

@app.route('/convert', methods=['GET', 'POST'])
def convert_form():
    if request.method == 'POST':
        try:
            celsius = float(request.form['celsius'])
            fahrenheit = celsius_to_fahrenheit(celsius)
            return f"<h2>{celsius:.2f}°C = {fahrenheit:.2f}°F</h2>"
        except ValueError:
            return "<h2>Invalid input. Please enter a number.</h2>"

    return '''
        <form method="post">
            Enter Celsius temperature: <input name="celsius">
            <input type="submit" value="Convert">
        </form>
    '''

if __name__ == '__main__':
    app.run()
