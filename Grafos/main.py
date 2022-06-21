import networkx as nx
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk, Text
from tkinter import *
from PIL import Image, ImageTk
import time
import numpy as np
from networkx import DiGraph, Graph, simple_cycles
import pandas as pd
import scipy as sp

tempo_inicial = (time.time())
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
    file = file.split(',')
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
        file = file.split(',')
        cor = file[1]
    else:
        break

    for l in range(int(file[2])):
        file2 = fi2.readline()
        edge = file2.split(',')
        for i in range(n):
            if edge[0] == nome[i]:
                temp = i

        for j in range(n):
            if edge[1] == nome[j]:
                temp2 = j

        g.add_edge(etc[temp], etc[temp2], color=cor)

node_label_options = {"font_size": 6,
                      "verticalalignment": "bottom"}

node_options = {"node_size": 35}

edge_options = {"width": 1.5}
default = ndcor

colors = nx.get_edge_attributes(g, 'color').values()
nomes2 = nx.get_node_attributes(g, 'nomes')
ndcolor = nx.get_node_attributes(g, 'nodecolor').values()
pos = nx.get_node_attributes(g, 'pos')
nx.draw(g, pos, labels=nomes2, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options,
        **node_options, **edge_options)
plt.savefig("grafo.png")


def Funcao1():
    tempo1 = (time.time())
    pos = nx.get_node_attributes(g, 'pos')
    total = 10000;
    if Lista1.get() != "" and Lista2.get() != "":
        for l in range(len(nome)):
            for i in range(n):
                if Lista1.get() == nome[i]:
                    temp = i + 1

            for j in range(n):
                if Lista2.get() == nome[j]:
                    temp2 = j + 1

        F1 = (nx.all_simple_paths(g, source=temp, target=temp2))
        l = list(F1)
        for j in range(len(l)):
            distancia = 0
            e = nx.subgraph(g, l[j])
            t = list(e.edges)
            for i in range(len(t)):
                x1 = (pos[t[i][0]][0])
                y1 = (pos[t[i][0]][1])
                x2 = (pos[t[i][1]][0])
                y2 = (pos[t[i][1]][1])
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distancia = distancia + distance
            if total > distancia:
                total = distancia
                print(total)
                v = j
                print(l[v])

        h = nx.subgraph(g, l[v])
        colors = nx.get_edge_attributes(h, 'color').values()
        nomes2 = nx.get_node_attributes(h, 'nomes')
        ndcolor = nx.get_node_attributes(h, 'nodecolor').values()
        pos = nx.get_node_attributes(h, 'pos')
        plt.figure()
        nx.draw(h, pos, labels=nomes2, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options,
                **node_options, **edge_options)
        plt.savefig("Funcao1.png")
        global my_img1
        top1 = Toplevel()
        top1.title('Funcao 1')
        my_img1 = ImageTk.PhotoImage(Image.open("Funcao1.png"))
        my_label1 = Label(top1, image=my_img1).grid(row=0, column=0)
        tempo1_final = (time.time())
        print(f"{tempo1_final - tempo1} segundos")


def Funcao2():
    tempo2 = (time.time())
    if Lista1.get() != "" and Lista2.get() != "":
        for l in range(len(nome)):
            for i in range(n):
                if Lista1.get() == nome[i]:
                    temp = i + 1

            for j in range(n):
                if Lista2.get() == nome[j]:
                    temp2 = j + 1

        F2 = (nx.shortest_path(g, source=temp, target=temp2))
        print(F2)
        h = nx.subgraph(g, F2)
        colors = nx.get_edge_attributes(h, 'color').values()
        nomes2 = nx.get_node_attributes(h, 'nomes')
        ndcolor = nx.get_node_attributes(h, 'nodecolor').values()
        pos = nx.get_node_attributes(h, 'pos')
        plt.figure()
        nx.draw(h, pos, labels=nomes2, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options,
                **node_options, **edge_options)
        plt.savefig("Funcao2.png")
        global my_img2
        top2 = Toplevel()
        top2.title('Funcao 2')
        my_img2 = ImageTk.PhotoImage(Image.open("Funcao2.png"))
        my_label2 = Label(top2, image=my_img2).grid(row=0, column=0)
        print(h.nodes)
        tempo2_final = (time.time())
        print(f"{tempo2_final - tempo2} segundos")


def Funcao3():
    tempo3 = (time.time())
    total = 1000;
    if Lista1.get() != "" and Lista2.get() != "":
        for l in range(len(nome)):
            for i in range(n):
                if Lista1.get() == nome[i]:
                    temp = i + 1

            for j in range(n):
                if Lista2.get() == nome[j]:
                    temp2 = j + 1

        F3 = (nx.all_simple_paths(g, source=temp, target=temp2))
        l = list(F3)
        for j in range(len(l)):
            e = nx.subgraph(g, l[j])
            t = list(e.edges)
            corlinha = list(range(1, len(t) + 1))

            for i in range(len(t)):
                corlinha[i] = g.edges[t[i]]['color']

            corlinha = list(dict.fromkeys(corlinha))
            if len(corlinha) < total:
                total = len(corlinha)
                sub = j

        h = nx.subgraph(g, l[sub])
        colors = nx.get_edge_attributes(h, 'color').values()
        nomes2 = nx.get_node_attributes(h, 'nomes')
        ndcolor = nx.get_node_attributes(h, 'nodecolor').values()
        pos = nx.get_node_attributes(h, 'pos')
        plt.figure()
        nx.draw(h, pos, labels=nomes2, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options,
                **node_options, **edge_options)
        plt.savefig("Funcao3.png")
        global my_img3
        top3 = Toplevel()
        top3.title('Funcao 3')
        my_img3 = ImageTk.PhotoImage(Image.open("Funcao3.png"))
        my_label3 = Label(top3, image=my_img3).grid(row=0, column=0)
        tempo3_final = (time.time())
        print(f"{tempo3_final - tempo3} segundos")


def Funcao4():
    tempo4 = (time.time())
    lista = list(range(1, len(nome) + 1))
    total = 100
    for j in range(len(lista)):
        edges = []
        for i in range(len(lista)):
            if etc[j] != lista[i]:
                F4 = (nx.shortest_path(g, source=etc[j], target=lista[i]))
                h = nx.subgraph(g, F4)
                edges = edges + list(h.edges)
        h = g.edge_subgraph(edges)
        if total > len(h.edges):
            total = len(h.edges)
            tmp = j
    edges = []
    for i in range(len(lista)):
        if etc[tmp] != lista[i]:
            F4 = (nx.shortest_path(g, source=etc[tmp], target=lista[i]))
            h = nx.subgraph(g, F4)
            edges = edges + list(h.edges)

    h = g.edge_subgraph(edges)
    colors = nx.get_edge_attributes(h, 'color').values()
    nomes2 = nx.get_node_attributes(h, 'nomes')
    ndcolor = nx.get_node_attributes(h, 'nodecolor').values()
    pos = nx.get_node_attributes(h, 'pos')
    plt.figure()
    nx.draw(h, pos, labels=nomes2, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options,
            **node_options, **edge_options)
    plt.savefig("Funcao4.png")
    global my_img4
    top4 = Toplevel()
    top4.title('Funcao 4')
    my_img4 = ImageTk.PhotoImage(Image.open("Funcao4.png"))
    my_label4 = Label(top4, image=my_img4).grid(row=0, column=0)
    my_label = Label(top4, text=len(h.edges)).grid(row=1, column=0)
    tempo4_final = (time.time())
    print(f"{tempo4_final - tempo4} segundos")


def Funcao5():
    tempo5 = (time.time())
    h2 = nx.eulerize(g)
    h2l = list(nx.eulerian_circuit(h2))
    h = g.edge_subgraph(h2l)
    node_label_options = {"font_size": 10,
                          "verticalalignment": "bottom"}
    nomes2 = nx.get_node_attributes(h, 'nomes')
    ndcolor = nx.get_node_attributes(h, 'nodecolor').values()
    pos = nx.get_node_attributes(h, 'pos')
    plt.figure()
    nx.draw(h, pos, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options,
            **node_options, **edge_options)
    plt.savefig("Funcao5.png")
    global my_img5
    top5 = Toplevel()
    top5.title('Funcao 5')
    my_img5 = ImageTk.PhotoImage(Image.open("Funcao5.png"))
    my_label5 = Label(top5, image=my_img5).grid(row=0, column=0)
    text = Label(top5, text=h2l[:31], font=1).grid(row=1, column=0)
    text2 = Label(top5, text=h2l[31:], font=1).grid(row=2, column=0)
    tempo5_final = (time.time())
    print(f"{tempo5_final - tempo5} segundos")


def Funcao6():
    tempo6 = (time.time())
    lista = list(range(1, len(nome) + 1))
    total = 0
    for j in range(len(lista)):
        for i in range(len(lista)):
            F6 = list((nx.all_simple_paths(g, source=etc[i], target=etc[j])))
            for k in range(len(F6)):
                if total < len(F6[k]):
                    total = len(F6[k])
                    nodes = F6[k]

    h = g.subgraph(nodes)
    node_label_options = {"font_size": 10,
                          "verticalalignment": "bottom"}
    nomes2 = nx.get_node_attributes(h, 'nomes')
    ndcolor = nx.get_node_attributes(h, 'nodecolor').values()
    pos = nx.get_node_attributes(h, 'pos')
    plt.figure()
    nx.draw(h, pos, with_labels=True, edge_color=colors, node_color=ndcolor, **node_label_options,
            **node_options, **edge_options)
    plt.savefig("Funcao6.png")
    global my_img6
    top6 = Toplevel()
    top6.title('Funcao 6')
    my_img6 = ImageTk.PhotoImage(Image.open("Funcao6.png"))
    my_label6 = Label(top6, image=my_img6).grid(row=0, column=0)
    text = Label(top6, text=nodes).grid(row=1, column=0)
    text2 = Label(top6, text=len(nodes)).grid(row=2, column=0)
    tempo6_final = (time.time())
    print(f"{tempo6_final - tempo6} segundos")


def Funcao7():
    tempo7 = (time.time())
    lista = etc
    total = 100

    for i in range(len(lista)):
        ndcor = default
        tmp = list(nx.neighbors(g, lista[i]))
        ndcor[lista[i] - 1] = 'red'
        for j in range(len(lista)):
            bol = 0
            tmp2 = list(nx.neighbors(g, lista[j]))
            if len(tmp2) <= 1:
                ndcor[lista[j] - 1] = 'black'
                ndcor[tmp2[0]] = 'red'
            if ndcor[lista[j] - 1] != 'red' and ndcor[lista[j] - 1] != 'black':
                tmp4 = 0
                for k in range(len(tmp2)):
                    if ndcor[tmp2[k] - 1] != 'red':
                        ndcor[tmp2[k] - 1] = 'red'
                for k in range(len(tmp2)):
                    if ndcor[tmp2[k] - 1] == 'black':
                        tmp4 = tmp4 + 1
                if len(tmp2) == tmp4:
                    ndcor[lista[j] - 1] = 'red'
            if ndcor[lista[j] - 1] == 'red':
                for k in range(len(tmp2)):
                    ndcor[tmp2[k] - 1] = 'black'
            if ndcor[lista[j] - 1] == 'black':
                tmp4 = 0
                for k in range(len(tmp2)):
                    if ndcor[tmp2[k] - 1] == 'black':
                        tmp4 = tmp4 + 1
                if len(tmp2) == tmp4:
                    ndcor[lista[j] - 1] = 'red'
                if len(tmp2) > tmp4 and tmp4 >= 0:
                    ndcor[lista[j] - 1] = 'black'
        for j in reversed(lista):
            bol = 0
            tmp2 = list(nx.neighbors(g, lista[j - 1]))
            if ndcor[lista[j - 1] - 1] == 'red':
                for t in range(len(tmp2)):
                    if ndcor[tmp2[t] - 1] == 'red':
                        for k in range(len(tmp2)):
                            ndcor[tmp2[k] - 1] = 'black'
            if ndcor[lista[j - 1] - 1] == 'black':
                tmp4 = 0
                for k in range(len(tmp2)):
                    if ndcor[tmp2[k] - 1] == 'black':
                        tmp4 = tmp4 + 1
                if len(tmp2) == tmp4:
                    ndcor[lista[j - 1] - 1] = 'red'
                if len(tmp2) > tmp4 and tmp4 > 0:
                    ndcor[lista[j - 1] - 1] = 'black'
        n = 0
        for h in range(len(ndcor)):
            if ndcor[h] == 'red':
                n = n + 1
        if n <= total:
            total = n
            cormaximal = ndcor

    colors = nx.get_edge_attributes(g, 'color').values()
    nomes2 = nx.get_node_attributes(g, 'nomes')
    ndcolor = nx.get_node_attributes(g, 'ndcor').values()
    pos = nx.get_node_attributes(g, 'pos')
    plt.figure()
    nx.draw(g, pos, labels=nomes2, with_labels=True, edge_color=colors, node_color=cormaximal, **node_label_options,
            **node_options, **edge_options)
    plt.savefig("Funcao7.png")
    global my_img7
    top7 = Toplevel()
    top7.title('Funcao 7')
    my_img7 = ImageTk.PhotoImage(Image.open("Funcao7.png"))
    my_label4 = Label(top7, image=my_img7).grid(row=0, column=0)
    label = Label(top7, text=total).grid(row=1, column=0)
    tempo7_final = (time.time())
    print(f"{tempo7_final - tempo7} segundos")


# Interface Gráfica
root = tk.Tk()
root.title("Grafos")
root.configure(bg='black')
photo = tk.PhotoImage(file="grafo.png", master=root)
label1 = tk.Label(root, bg="black", fg="white").grid(row=0, column=0)
label2 = tk.Label(root, image=photo).grid(rowspan=7, column=2)
Lista1 = ttk.Combobox(root, values=nome)
Lista1.grid(row=0, column=0)
Lista2 = ttk.Combobox(root, values=nome)
Lista2.grid(row=0, column=1)
Button1 = tk.Button(root, text='Funcao1', padx=50, command=Funcao1).grid(row=1, columnspan=2)
Button2 = tk.Button(root, text='Funcao2', padx=50, command=Funcao2).grid(row=2, columnspan=2)
Button3 = tk.Button(root, text='Funcao3', padx=50, command=Funcao3).grid(row=3, columnspan=2)
Button4 = tk.Button(root, text='Funcao4', padx=50, command=Funcao4).grid(row=4, columnspan=2)
Button5 = tk.Button(root, text='Funcao5', padx=50, command=Funcao5).grid(row=5, columnspan=2)
Button6 = tk.Button(root, text='Funcao6', padx=50, command=Funcao6).grid(row=6, columnspan=2)
Button7 = tk.Button(root, text='Funcao7', padx=50, command=Funcao7).grid(row=7, columnspan=2)
tempo_final = (time.time())
print(f"{tempo_final - tempo_inicial} segundos")
root.mainloop()
