import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def create_graph(N):
  G = nx.MultiGraph()
  for i in range(1, N * N):
    G.add_node(i)
  for j in range(1, N * N):
    if ((j-1) // N == (j) // N):
      G.add_edge(j, j + 1)
    if (j / N <= N - 1):
      G.add_edge(j, j + N)
  return G

def create_color(N):
  color = ['blue'] * N * N
  for i in range (N,0):
    color[i] = color[i-1]
  return color

def create_pos(G, N):
    pos = {}
    for node in G.nodes:
      pos[node] = ((node-1)%N, N-(node-1)//N)
    return pos

def create_obstacle_simple(G, i):
    edges = list(G.edges(i))
    for i in range (len(edges)):
      G.remove_edge(edges[i][0], edges[i][1])
    return G

def create_obstacle(G, X_start,  X_end, Y_start, Y_end, N, color):
  for i in range (X_end - X_start+1):
    for j in range (Y_end - Y_start+1):
      G = create_obstacle_simple(G, (X_start+i)+N*(Y_start+j)-N)
      color[(X_start+i-1)+N*(Y_start+j)-N] = 'black'
  return G, color

def create_robot(X, Y, N, color):
  color[(X-1)+N*(Y)-N] = 'red'
  return color

def create_trash(X, Y, N, color):
  color[(X-1)+N*(Y)-N] = 'yellow'
  return color

graphe = create_graph(8)
pos_fix = create_pos(graphe, 8)
colors = create_color(8)
graphe, colors = create_obstacle(graphe, 1, 3, 4, 7, 8, colors)
colors = create_robot(4, 4, 8, colors)
colors = create_trash(5,6,8,colors)
colors = create_trash(1,1,8,colors)
colors = create_trash(5,5,8,colors)
colors = create_trash(4,7,8,colors)
nx.draw(graphe, pos=pos_fix, with_labels=True, node_color=colors)
labels = nx.get_edge_attributes(graphe, 1)
plt.show()