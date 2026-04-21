import os 
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Error (÷0)"
    return "Invalid"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    app_name = os.environ.get("APP_NAME", "Default App")

    if request.method == "POST":
        a = float(request.form["num1"])
        b = float(request.form["num2"])
        op = request.form["operation"]
        result = calculate(a, b, op)

    return render_template("index.html", result=result, app_name=app_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)