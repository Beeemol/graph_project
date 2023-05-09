""" fonction A*(s,t : sommet , G : graphe) : booléen,tableau de réels , tableau de sommets
début
	(d,parent) ← initialisation(s,G);
	GRIS ← vide() ; 
	ajouter(s,GRIS) ; 
	NOIR ← vide() ; 
		
	tantque vrai() faire
	debut
		si estVide(GRIS) alors 
			retourner (faux(),d,parent);
		x ← calculer_d+h_Min(GRIS,d,G) ;
		si x = t alors 
			retourner (vrai(),d,parent);
		L ← listeArcsSortants(x,G) ; 

		pour i de 1 à longueur(L) faire
			relâcherA*(iemeArc(i,L),G,d,parent,GRIS,NOIR)
		;
		colorerEnNoir(x,GRIS,NOIR)
	fin			
fi

fonction relâcherA*(e: arc,G,d,parent,GRIS,NOIR)
début
	(x,y) ← extrémités(e,G);
		si d[x]+poids(e,G) < d[y] alors
	début
		d[y] ← d[x]+poids(e,G);
		parent[y] ← x ; 
		colorerEnGris(y,GRIS,NOIR)
	fin
fi	

procédure colorerEnGris(y:sommet,GRIS:ensemble,NOIR:ensemble)
	début
	si appartient(y,NOIR) alors
		enlever(y,NOIR)
	;
	ajouter(y,GRIS)
fin


fonction DIJKSTRA(s : sommet , G : graphe) :tableau de réels , tableau de sommets
début
    (d,parent) ← initialisation(s,G)
    nonNOIR ← ensemble_sommets(G)	
    faire nbreSommets(G) fois 
    debut
        x ← extraireMin(nonNOIR,d) ; 
        L ← listeArcsSortants(x,G) ;	
        pour i de 1 à longueur(L) faire
            relâcher(iemeArc(i,L),G,d,parent,nonNOIR)
    fin
    retourner(d,parent)
fin """

import networkx as nx
import heapq
from graphs import *


""" Retourne la liste des positions des déchets sur le graphe """
def list_trash_pos(colors):
    pos = []
    for i in range(0, len(colors), 1):
        if colors[i] == 'yellow':
            pos.append(i+1)
    return pos


""" Donne la position du robot dans le graphe """
def robot_pos(colors):
    for i in range(0, len(colors), 1):
        if colors[i] == 'red':
            return i+1

""" Parcours le graphe G depuis un sommet start_node vers un sommet end_node en 
cherchant le chemin plus court selon l'algorithme de Dijkstra """
def dijkstra_shortest_path(G, start_node, end_node):

    visited = {start_node: 0}
    heap = [(0, start_node)]
    path = {}

    while heap:
        (dist, current_node) = heapq.heappop(heap)

        if current_node == end_node:
            """ Retourne le chemin le plus court et sa distance """
            shortest_path = []
            while current_node in path:
                shortest_path.append(current_node)
                current_node = path[current_node]
            shortest_path.append(start_node)
            shortest_path.reverse()
            return (dist, shortest_path)

        if current_node in visited and visited[current_node] < dist:
            continue

        for neighbor in G.neighbors(current_node):
            tentative_distance = dist + G[current_node][neighbor][0]['weight']
            if neighbor not in visited or tentative_distance < visited[neighbor]:
                visited[neighbor] = tentative_distance
                heapq.heappush(heap, (tentative_distance, neighbor))
                path[neighbor] = current_node

    """ Retourne None si aucun chemin n'a été trouvé """
    return None

""" Retourne la somme des éléments d'un tableau donné en paramètre """
def sum(array):
    sum = 0
    for i in array:
        sum+=i
    return sum

def main():

    """ Création d'un graphe de taille N """
    N=20
    graphe = create_graph(N)
    colors = create_color(N)
    graphe, colors = create_obstacle(graphe, 1, 3, 4, 7, N, colors)
    colors = create_robot(4, 4, N, colors)
    colors = create_trash(5,6,N,colors)
    colors = create_trash(1,1,N,colors)
    colors = create_trash(5,5,N,colors)
    colors = create_trash(4,7,N,colors)

    """ Créé une liste de position associée a chaque sommet : utile 
    pour l'affichage du grpahe seulement """
    pos_fix = create_pos(graphe, N)
    
    """ Affichage du graphe """
    nx.draw(graphe, pos=pos_fix, with_labels=True, node_color=colors)
    labels = nx.get_edge_attributes(graphe, 1)
    plt.show()

    trash_pos=list_trash_pos(colors)

    shortest_path = []
    shortest_path_cost = []

    start = 0
    end = robot_pos(colors)

    tmp=0

    """ Recherche du plus court chemin """
    for i in range(0, len(trash_pos), 1):
        start = end
        end = trash_pos[i]
        if(dijkstra_shortest_path(graphe, start, end) == None):
            print("ERROR: Chemin inexistant. Veuillez vérifier votre graphe et le corriger.")
            tmp=1
            break
        shortest_path_cost.append(dijkstra_shortest_path(graphe, start, end)[0])
        shortest_path.append(dijkstra_shortest_path(graphe, start, end)[1])

    if(tmp==0):
        print("chemin le plus court entre les déchets:", shortest_path)
        print("cout de chaque chemin:", shortest_path_cost)
        print("cout total:", sum(shortest_path_cost))

if __name__ == "__main__":
    main()