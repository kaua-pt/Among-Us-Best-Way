class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adicionarAresta(self, pontoA, pontoB, custo):
        self.grafo[pontoA-1][pontoB-1] = custo
        self.grafo[pontoB-1][pontoA-1] = custo

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])
