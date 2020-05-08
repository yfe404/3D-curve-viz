import os.path
from flask import render_template
from flask import Flask

app = Flask(
    __name__,
    static_url_path="{}/static".format(os.path.abspath(os.path.dirname(__file__))),
)


def load_curve(curve_id):
    """
    Load a curve from a dataset

    :param curve_id: integer, index of the curve
    :return: Curve object 
    """
    raise NotImplementedError


@app.route("/<int:curve_id>")
def index(curve_id):
    points = load_curve(curve_id)
    center = [
        sum([p[0] for p in points]) / len(points),
        sum([p[1] for p in points]) / len(points),
        sum([p[2] for p in points]) / len(points),
    ]
    print(len(points))
    return render_template("shape.html", points=points, center=center)


if __name__ == "__main__":
    app.run()
