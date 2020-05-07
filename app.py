import os.path
from flask import render_template
from flask import Flask

app = Flask(
    __name__,
    static_url_path="{}/static".format(os.path.abspath(os.path.dirname(__file__))),
)


@app.route("/")
def index():
    points = [[0, 0, 0], [-32, -12, 8]]
    return render_template("shape.html", points=points)


if __name__ == "__main__":
    app.run()
