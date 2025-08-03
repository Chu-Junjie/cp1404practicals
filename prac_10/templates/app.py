from flask import Flask, request, render_template

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


@app.route('/')
def hello_world():
    """Homepage greeting."""
    return "<h1>Hello World :)</h1>"


@app.route('/f/<celsius>')
def convert_url(celsius):
    """Convert Celsius from URL to Fahrenheit."""
    try:
        celsius_value = float(celsius)
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        return f"{celsius_value:.2f}°C = {fahrenheit_value:.2f}°F"
    except ValueError:
        return "Invalid input. Please enter a number like /f/36.5"


@app.route('/convert', methods=['GET', 'POST'])
def convert_form():
    """Form: Convert Celsius to Fahrenheit."""
    result = ""
    if request.method == 'POST':
        try:
            celsius = float(request.form['celsius'])
            fahrenheit = celsius_to_fahrenheit(celsius)
            return f"<h2>{celsius:.2f}°C = {fahrenheit:.2f}°F</h2>"
        except ValueError:
            return "<h2>Invalid input. Please enter a number.</h2>"

    return render_template("convert.html", result=result)


@app.route('/convert_f', methods=['POST'])
def convert_f_form():
    """Form: Convert Fahrenheit to Celsius."""
    result_f = ""
    try:
        fahrenheit = float(request.form['fahrenheit'])
        celsius = fahrenheit_to_celsius(fahrenheit)
        result_f = f"{fahrenheit:.2f}°F = {celsius:.2f}°C"
    except ValueError:
        result_f = "Invalid input. Please enter a number."
    return render_template("convert.html", result="", result_f=result_f)


if __name__ == '__main__':
    app.run()
