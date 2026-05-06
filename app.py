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
    import os
    import shutil
    from flask import render_template

    build_dir = "build"

    # Clean build directory
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)

    with app.app_context():
        html = render_template("index.html")
        with open(os.path.join(build_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)

    # Copy static assets
    if os.path.exists("static"):
        shutil.copytree(
            "static",
            os.path.join(build_dir, "static"),
        )

    # Ensure GitHub Pages does not use Jekyll
    open(os.path.join(build_dir, ".nojekyll"), "w").close()

    print("✅ Build complete")


# -----------------------
# Entry point
# -----------------------

if __name__ == "__main__":
    if "build" in sys.argv:
        build()
    else:
        app.run(debug=True)