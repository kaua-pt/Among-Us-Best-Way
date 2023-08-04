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

            vizinhos = self.grafo.neighbors(menorNo)

            for vizinho in vizinhos:
                tentativa = menorCaminho[menorNo] + \
                    self.grafo.get_edge_data(menorNo, vizinho)['peso']
                if tentativa < menorCaminho[vizinho]:
                    menorCaminho[vizinho] = tentativa
                    nosAnteriores[vizinho] = menorNo

            nosNaoVisitados.remove(menorNo)
        return menorCaminho
