#imports#

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory

#flask app#

app = Flask(__name__)
app.config['SECRET_KEY'] = 'srg6789$*&@B#*BB*s$%^&*'

#routes#

@app.route('/')
def home():
    return render_template("index.html")

#start server code#

if __name__ == "__main__":
    app.run(debug=True)

