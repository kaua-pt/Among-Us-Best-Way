from flask import Blueprint, render_template, request as req
from .utils import tasks
from .graph.GerarGrafo import gerarGrafo
from .graph.Dijkstra import Dijkstra
import sys

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
    dij = Dijkstra(G)
    tasksE = list(req.form.keys())
    taskPlace = []
    path = []

    # tempo de realização das tasks
    for taskE in tasksE:
        if (taskE in tasks):
            time += tasks[taskE]['tempo']

    # tratar dados
    for taskE in tasksE:
        taskPlace.append(tasks[taskE]['local'])

    # tempo ótimo para percorrer as tasks
    lastLocal = ""
    begin = "Cafeteria"
    taskPlace.sort()
    for i in range(len(taskPlace)):
        menor = ""
        menorPeso = sys.maxsize
        path.append(begin)

        if lastLocal in taskPlace:
            time += G.get_edge_data(begin, begin)['peso']
            taskPlace.remove(lastLocal)
        else:
            distancias = dij.encontrarCaminho(begin, taskPlace)
            for element in taskPlace:
                for element2 in distancias:
                    if (element == element2 and distancias[element] < menorPeso):
                        menorPeso = distancias[element]
                        menor = element

            time += menorPeso
            lastLocal = begin
            begin = menor
            taskPlace.remove(menor)
    path.append(menor)

    return render_template("map.html", time=round(time, 2), path=path)
