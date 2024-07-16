from flask import Flask, render_template_string

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"

# Print string route
@app.route('/print/<string>')
def print_string(string):
    print(f"Printing string: {string}")
    return string

# Count route
@app.route('/count/<int:num>')
def count(num):
    numbers = "\n".join(str(i) for i in range(1, num + 1))
    return numbers

# Math route
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is undefined."
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Modulo by zero is undefined."
    else:
        return "Error: Invalid operation. Please use one of '+', '-', '*', 'div', '%'."

    return f"The result of {num1} {operation} {num2} is {result}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
