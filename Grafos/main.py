import networkx as nx
from matplotlib import pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk

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


etc = list(range(1, n + 1))


for i in range(n):
    g.add_node(etc[i], pos=(x[i], y[i]), nodecolor=ndcor[i], nomes=nome[i])  # cria aresta e suas cordenadas

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

node_label_options = {"font_size": 10,
                      "verticalalignment": "bottom"}

node_options = {"node_size": 35}

edge_options = {"width": 1.5}

colors = nx.get_edge_attributes(g, 'color').values()
nomes2 = nx.get_node_attributes(g, 'nomes')
ndcolor = nx.get_node_attributes(g, 'nodecolor').values()
pos = nx.get_node_attributes(g, 'pos')
print(type(pos))
nx.draw(g, pos, labels=nomes2, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options, **node_options, **edge_options)
plt.savefig("grafo.png")

p = list(nx.all_simple_paths(g, source=4, target=6))
h = nx.subgraph(g, p[0])
e = list(h.edges)
print(e[1])
print(g.edges[e[1]]['color'])
print(g.nodes)


#Interface Gráfica
root = tk.Tk()
root.title("ola")
root.configure(bg='black')
photo = tk.PhotoImage(file="grafo.png")
label = tk.Label(root, text="Grafo", bg="black", fg="white").grid(row=1, column=0)
label1 = tk.Label(root,bg="black", fg="white").grid(row=0, column=0)
label2 = tk.Label(root, image=photo).grid(row=1, column=1)
root.mainloop()