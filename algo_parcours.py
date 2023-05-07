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
