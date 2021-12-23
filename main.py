from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/bible")
def bible():
    return render_template('bible.html')

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")