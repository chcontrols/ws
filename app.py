from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def build():
    os.makedirs("build", exist_ok=True)
    with app.app_context():
        html = render_template("index.html")
        with open("build/index.html", "w") as f:
            f.write(html)

if __name__ == "__main__":
    app.run(debug=True)

    