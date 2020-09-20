from flask import Flask, redirect, url_for, render_template, request
import os
from index import gui_run

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            gui_run()
            return render_template("index.html")
    else:
        return render_template("index.html")


@app.route('/about')
def about():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
