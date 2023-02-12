from flask import Blueprint, redirect, url_for

bp = Blueprint("root", __name__)

@bp.route("/")
def index():
    return redirect(url_for("test.test_handler"))