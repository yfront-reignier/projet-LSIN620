class AutomateCellulaire:
    # Question 1
    def __init__(self, etats, regles):
        """
        Initialise un automate cellulaire.
        :param etats: Ensemble des états possibles pour les cellules (par exemple, {0, 1}).
        :param regles: Dictionnaire représentant la fonction de transition.
                       Chaque clé est un triplet (gauche, centre, droite),
                       et la valeur est le nouvel état du centre.
        """
        # Stocke l'ensemble des états possibles pour les cellules.
        self.etats = etats
        # Stocke les règles de transition sous forme de dictionnaire.
        # Exemple : {(0, 0, 1): 1, (1, 1, 0): 0}
        self.regles = regles
    
    def appliquer_regle(self, voisinage):
        """
        Applique la règle de transition sur un triplet de cellules.
        :param voisinage: Tuple représentant l'état des cellules voisines (gauche, centre, droite).
                          Exemple : (0, 1, 0)
        :return: Nouvel état du centre après application de la règle.
        """
        # Recherche la règle correspondant au triplet donné dans le dictionnaire.
        # Si le triplet n'est pas défini dans les règles, on retourne l'état actuel du centre (voisinage[1]).
        return self.regles.get(voisinage, voisinage[1])  # Par défaut, on garde l'état actuel.