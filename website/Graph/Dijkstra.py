import heapq
import sys


class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
        self.distance = 0

    def encontrarCaminho(self, origem, tasks):
        nosNaoVisitados = list(self.grafo.nodes())
        menorCaminho = {}
        nosAnteriores = {}
        infinity = sys.maxsize

        for no in nosNaoVisitados:
            menorCaminho[no] = infinity
        menorCaminho[origem] = 0

        while nosNaoVisitados:
            menorNo = None
            for no in nosNaoVisitados:
                if menorNo == None:
                    menorNo = no
                elif menorCaminho[no] < menorCaminho[menorNo]:
                    menorNo = no
        vizinhos = self.grafo
