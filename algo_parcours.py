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

# Idée: on a le tableau des pos des déchets, et la position initiale du robot.
# On boucle dijsktra entre la position i et la position i+1 de ces coordonnées
# On retourne les chemins obtenus


import networkx as nx
import heapq

def create_graph(N):
    G = nx.MultiGraph()
    for i in range(1, N * N):
        G.add_node(i)
    for j in range(1, N * N):
        if ((j-1) // N == (j) // N):
            G.add_edge(j, j + 1, weight=1)
        if (j / N <= N - 1):
            G.add_edge(j, j + N, weight=1)
    return G

def dijkstra_shortest_path(G, start_node, end_node):

    visited = {start_node: 0}
    heap = [(0, start_node)]
    path = {}

    while heap:
        (dist, current_node) = heapq.heappop(heap)

        if current_node == end_node:
            # Retourne le chemin le plus court et sa distance
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

    # Retourne None si aucun chemin n'a été trouvé
    return None

def main():
    N=8
    graphe = create_graph(N)

    shortest_path_cost, shortest_path = dijkstra_shortest_path(graphe, 1, N*N)
    print(shortest_path)
    print(shortest_path_cost)

if __name__ == "__main__":
    main()