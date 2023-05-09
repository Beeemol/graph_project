import numpy as np
import sys
import random
import matplotlib.pyplot as plt
import networkx as nx
from read import parse_elements_file

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print( "Veuillez donner le chemin d'un fichier en arguments du programme")
        exit(1)
        
        
    elements = parse_elements_file(sys.argv[1])
    print(elements)

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
def random_trash(N, K, color):
  i = 0
  while(i != K):
    r1 = random.randint(1, N)
    r2 = random.randint(1, N)
    if(color[(r1-1) + N*r2-N] == 'blue'):
      color = create_trash(r1,r2,N,color)
      i = i + 1
  return color
    


def initialize_world(elements, N):
  graph = create_graph(N)
  pos_fix = create_pos(graph, N)
  colors = create_color(N)

  for i in range (len(elements)):
    if(elements[i].name == 'R'):
      colors = create_robot(elements[i].start_x, elements[i].start_y, N, colors)
    if(elements[i].name == 'X'):
      graph, colors = create_obstacle(graph, elements[i].start_x, elements[i].end_x, elements[i].start_y, elements[i].end_y, N, colors)
    if(elements[i].name.isdigit()):
      colors = create_trash(elements[i].start_x, elements[i].start_y, N, colors)

  nx.draw(graph, pos=pos_fix, with_labels=True, node_color=colors)
  return graph

def initialize_world_random_no_obstacle(N, K):
  graph = create_graph(N)
  pos_fix = create_pos(graph, N)
  colors = create_color(N)
  colors = create_robot(N//2, N//2, N, colors)
  colors = random_trash(N, K, colors) 

  nx.draw(graph, pos=pos_fix, with_labels=True, node_color=colors)
  return graph

initialize_world_random_no_obstacle(20, 4)
plt.show()