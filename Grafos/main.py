import networkx as nx
from matplotlib import pyplot as plt

with open(r"Estacoes.txt", 'r') as fp:  # Conta numero de linhas no arquivo
    n = len(fp.readlines())

filename = "Estacoes.txt"
fi = open(filename, "r")

g = nx.Graph()

nome = list(range(0, n))
x = list(range(0, n))
y = list(range(0, n))
ndcor = list(range(0, n))

for i in range(n):  # Le o arquivo com as estações e coordenadas, e armazena elas
    file = fi.readline()
    file = file.split()
    nome[i] = file[0]
    x[i] = file[1]
    y[i] = file[2]
    ndcor[i] = file[3]

x = [int(i) for i in x]
y = [int(i) for i in y]

nomes = {}
etc = list(range(1, n + 1))

for j in range(n):
    nomes[etc[j]] = nome[j]  # associa nome da estação com aresta

for i in range(n):
    g.add_node(etc[i], pos=(x[i], y[i]), nodecolor=ndcor[i])  # cria aresta e suas cordenadas

with open(r"Conexoes", 'r') as fp2:  # Conta numero de linhas no arquivo
    p = len(fp2.readlines())

filename = "Conexoes"
fi2 = open(filename, "r")
colors = {}

for k in range(p):
    file = fi2.readline()
    if file != "":
        file = file.split()
        cor = file[1]
        print(cor)
    else:
        break

    for l in range(int(file[2])):
        file2 = fi2.readline()
        edge = file2.split()
        print(edge)
        for i in range(n):
            if edge[0] == nome[i]:
                temp = i

        for j in range(n):
            if edge[1] == nome[j]:
                temp2 = j

        g.add_edge(etc[temp], etc[temp2], color =cor)


edges = g.edges()
colors = nx.get_edge_attributes(g, 'color').values()
ndcolor = nx.get_node_attributes(g, 'nodecolor').values()
pos = nx.get_node_attributes(g, 'pos')
nx.draw(g, pos, labels=nomes, with_labels=True, edge_color=colors, node_color=ndcolor)
plt.show()
