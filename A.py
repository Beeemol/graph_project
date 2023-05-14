import networkx as nx
import numpy as np
import heapq
from graphs import *
from enum import Enum
from itertools import permutations
import math
from algo_parcours import *

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4




def initialisation(s, G):
    d = {v: float('inf') for v in G}
    d[s] = 0
    parent = {v: None for v in G}
    return d,parent



def ListeArcsSortants(x,G):
    L=G.edges(x)
    return L

def appartient(y,L):
    for sommet in L:
        if sommet == y:
            return True
    return False

def enlever(y, L):
    NewL = []
    for sommet in L:
        if sommet != y:
            NewL.append(sommet)
    return NewL

def colorerEnGris(y, GRIS, NOIR):
    if y in NOIR:
        NOIR.remove(y)
    GRIS.append(y)

def colorerEnNoir(x, GRIS, NOIR):
    if appartient(x, GRIS): 
        enlever(x, GRIS)
    NOIR.append(x)

def relacherA(e, G, d, parent, GRIS, NOIR):
    x,y = e[0],e[1]
    if y not in NOIR and d[x] + G[x][y][0]['weight'] < d[y]:
        d[y] = d[x] + G[x][y][0]['weight']
        parent[y] = x
        colorerEnGris(y, GRIS, NOIR)

def calculer_d(d, GRIS):
    x = GRIS[-1]
    return d[x]
    
def Min_h(GRIS, d, t,n): #changer en manhatan
    s = GRIS[-1]
    xt = t % n 
    xs = s % n 
    yt = t // n
    ys = s // n
    return ((yt - ys)**2 + (xt - xs)**2)**0.5   


def change_direction( position, target_position, N):
    if position + 1 == target_position and position % N != (N-1): return Direction.EAST
    if position - 1 == target_position and position % N != 0: return Direction.WEST   
    if position + N == target_position: return Direction.SOUTH
    if position - N == target_position: return Direction.NORTH
    else: return 0

def time_change_direction(actual_direction, position, target_position, N, rotation_speed):
    new_direction = change_direction(position, target_position, N)
    if abs(new_direction - actual_direction) == 2: return 2*rotation_speed
    elif abs(new_direction - actual_direction) == 0: return 0
    elif abs(new_direction - actual_direction) == 1: return rotation_speed
    elif abs(new_direction - actual_direction) == 3: return rotation_speed

def heuristique(x,y,N):
    L = abs(x%N - y%N) 
    H = abs(x//N - y//N)
    return L+H


def A(s, t, G, N) :
    d, parent = initialisation(s,G)
    GRIS = []
    GRIS.append(s)
    NOIR = []

    while GRIS:

        x = min(GRIS, key= lambda v:d[v]+heuristique(v,t,N))
        
        if x == t:
            shortest_path = []
            while x!=s:
                shortest_path.append(x)
                x = parent[x]
            shortest_path.append(s)
            return (d[t], shortest_path[::-1])
    
        else :
            colorerEnNoir(x, GRIS, NOIR)
            L = ListeArcsSortants(x,G)
            for e in L:
                relacherA(e, G, d, parent, GRIS, NOIR)
    return float('inf'), []


