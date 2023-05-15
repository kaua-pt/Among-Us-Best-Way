from flask import Blueprint, render_template
from .utils import tasks

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", tasks=tasks)


@views.route('/map')
def map():
    return render_template("map.html")
