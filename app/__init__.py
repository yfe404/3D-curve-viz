import os.path
import numpy as np
from flask import render_template, url_for
from flask import Flask

app = Flask(
    __name__,
    static_folder="./static",
    static_url_path="{}/static".format(os.path.abspath(os.path.dirname(__file__))),
)


def load_curve(curve_id):
    """
    Load a curve from a dataset

    :param curve_id: integer, index of the curve
    :return: Curve object 
    """
    import scipy.io as sio

    data = sio.loadmat(url_for("static", filename="data/data_hommes.mat"))
    data = data["fH"]

    return data[:, :, curve_id]


@app.route("/<int:curve_id>")
def index(curve_id):
    points = load_curve(curve_id)

    velocity = np.gradient(points, axis=0).round(2)
    acceleration = np.gradient(velocity, axis=0).round(2)
    b_vector = np.cross(velocity, acceleration)
    print(b_vector.shape)
    n_vector = np.cross(b_vector, velocity)

    unit_tangeant = velocity  # / (np.sqrt(velocity.dot(velocity.T)))

    center = [
        sum([p[0] for p in points]) / len(points),
        sum([p[1] for p in points]) / len(points),
        sum([p[2] for p in points]) / len(points),
    ]
    print(len(points))
    return render_template(
        "shape.html",
        points=points,
        center=center,
        unit_tangeant=unit_tangeant,
        b_vector=b_vector,
        n_vector=n_vector,
    )
