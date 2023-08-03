from flask import Blueprint, render_template, request as req
from .utils import tasks
from .graph.GerarGrafo import gerarGrafo

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/select')
def select():
    return render_template("select.html", tasks=tasks)


@views.route('/map', methods=['POST', 'GET'])
def map():
    time = 0
    G = gerarGrafo()
    tasksE = list(req.form.keys())

    # tempo de realização das tasks
    for taskE in tasksE:
        if (taskE in tasks):
            print(taskE)
            time += tasks[taskE]['tempo']

    # tempo ótimo para percorrer as tasks
    #alg = dijkstra(G, taskE[0], tasksE)
    # print(alg)
    #time += alg['time']

    return render_template("map.html", time=time)
