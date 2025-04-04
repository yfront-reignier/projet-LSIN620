class Configuration:
    # Question 2
    def __init__(self, etat_initial):
        """
        Initialise une configuration d'un automate cellulaire.
        :param etat_initial: Liste représentant l'état initial des cellules.
        """
        # L'état actuel de la configuration est stocké sous forme de liste.
        self.etat = etat_initial
    
    def afficher(self):
        """
        Affiche la configuration sous forme lisible.
        """
        # Concatène les états des cellules en une chaîne de caractères et les affiche.
        print(''.join(str(cell) for cell in self.etat))
    
    def evoluer(self, automate):
        """
        Fait évoluer la configuration d'un pas de temps selon les règles de l'automate.
        :param automate: Instance de AutomateCellulaire
        """
        # Crée une nouvelle liste représentant l'état des cellules après évolution.
        nouvelle_etat = [
            # Applique la règle de transition de l'automate sur le voisinage de chaque cellule.
            automate.appliquer_regle((
                self.etat[i-1] if i > 0 else 0,  # Cellule de gauche (0 si en bordure gauche)
                self.etat[i],                   # Cellule actuelle
                self.etat[i+1] if i < len(self.etat)-1 else 0  # Cellule de droite (0 si en bordure droite)
            ))
            for i in range(len(self.etat))  # Parcourt toutes les cellules de la configuration.
        ]
        # Met à jour l'état actuel avec le nouvel état calculé.
        self.etat = nouvelle_etat