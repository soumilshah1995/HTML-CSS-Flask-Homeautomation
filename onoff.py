from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("Button was pressed ")

        if request.form['btn_on'] == "On":
            print("Pressed On")
            return render_template("onoff.html")

        if request.form['btn_on'] == "Off":
            print("Pressed On")
            return render_template("onoff.html")


    return render_template("onoff.html")


if __name__ == '__main__':
    app.run(debug=True)
