from flask import Blueprint, render_template, request as req
from .utils import tasks

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", tasks=tasks)


@views.route('/select')
def select():
    return render_template("select.html")


@views.route('/map')
def map():
    for element in tasks:
        if (req):
            print(req.form['id'])
    return render_template("map.html")
