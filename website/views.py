from flask import Blueprint, render_template, request as req
from .utils import tasks

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/select')
def select():
    return render_template("select.html", tasks=tasks)


@views.route('/map', methods=['POST', 'GET'])
def map():
    tasks = list(req.form.keys())

    return render_template("map.html")
