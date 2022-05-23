import networkx as nx
from matplotlib import pyplot as plt

with open(r"Estacoes.txt", 'r') as fp:   # Conta numero de linhas no arquivo
    n = len(fp.readlines())

filename = "Estacoes.txt"
fi = open(filename, "r")

g = nx.Graph()

nome = list(range(0, n))
x = list(range(0, n))
y = list(range(0, n))


for i in range(n):            # Le o arquivo com as estações e coordenadas, e armazena elas
    file = fi.readline()
    file = file.split()
    nome[i] = file[0]
    x[i] = file[1]
    y[i] = file[2]

nomes = {}
etc = list(range(1, n+1))

for j in range(n):
    nomes[etc[j]] = nome[j]     #associa nome da estação com aresta


for i in range(n):
    g.add_node(etc[i], pos=(x[i], y[i]))   #cria aresta e suas cordenadas


pos = nx.get_node_attributes(g, 'pos')
nx.draw(g, pos,labels=nomes, with_labels=True)
plt.show()


