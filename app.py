from flask import Flask, render_template
import os
import shutil
import sys

app = Flask(__name__)


# -----------------------
# Routes (dev only)
# -----------------------

@app.route("/")
def index():
    return render_template("index.html")


# -----------------------
# Static site builder
# -----------------------

def build():
    build_dir = "build"

    # Clean previous build
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)

    pages = {
        "index.html": "index.html",
    }

    with app.app_context():
        for output_file, template in pages.items():
            html = render_template(template)
            with open(os.path.join(build_dir, output_file), "w", encoding="utf-8") as f:
                f.write(html)

    # Copy static assets
    if os.path.exists("static"):
        shutil.copytree(
            "static",
            os.path.join(build_dir, "static"),
            dirs_exist_ok=True,
        )

    # Disable Jekyll on GitHub Pages
    open(os.path.join(build_dir, ".nojekyll"), "w").close()

    print("✅ Static site built successfully")


# -----------------------
# Entry point
# -----------------------

if __name__ == "__main__":
    if "build" in sys.argv:
        build()
    else:
        app.run(debug=True)