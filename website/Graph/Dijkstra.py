from .Grafo import Grafo
from .HeapMin import HeapMin


class Dijkstra:
    def __init__(self, vertices):
        self.grafo = Grafo(vertices)
        self.heap = HeapMin()

    def encontrarCaminho(self, origin):
        pass
