from flask import Blueprint, render_template

bp = Blueprint("test", __name__)


@bp.route("/test")
def test_handler():
    return render_template("test.html")