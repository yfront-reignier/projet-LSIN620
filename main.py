from sys import argv
from automate_cellulaire import AutomateCellulaire
from configuration import Configuration

# Question 3
def lectureFichier(fichier, initial):
    regles = recupConf(fichier)
    automate = AutomateCellulaire((0, 1), regles)

    conf_init = Configuration(initial)

    return (automate, conf_init)

def recupConf(fichier):
    configuration = {}
    with open(fichier, 'r') as f:
        for ligne in f:
            if ligne[0] not in ["0", "1", "2", "3"]:
                continue
            part_ligne = ligne.split('->')
            transitions = tuple(map(int, part_ligne[0].split(' ', 2)))
            nouv_etat = int(part_ligne[1][1])
            configuration[transitions] = nouv_etat
    return configuration

# Question 4
def calculAutomate(automate, configuration):
    configuration.evoluer(automate)
    configuration.afficher()

# Question 5
def calculAutomateArret(automate, mot, choix, n, transition):
    liste_mot = list(map(int, mot))
    conf = Configuration(liste_mot)
    
    if choix == '1':
        print("Calcul automate du temps t =", n)
        calculAutomateDonne(automate, conf, n)
    elif choix == '2':
        print("Calcul automate jusqu'à transition : ", transition)
        calculAutomateTransition(automate, conf, transition)
    elif choix == '3':
        print("Calcul automate pas de changement")
        calculAutomatePasDeChangement(automate, conf)

def calculAutomateDonne(automate,conf,n):
    for i in range(n):
        calculAutomate(automate, conf)
    return conf

def calculAutomateTransition(automate, conf, transition):
    print(conf.etat)
    while conf.etat != transition:
        conf.afficher()
        conf.evoluer(automate)
    return conf

def calculAutomatePasDeChangement(automate, conf):
    ancien_etat = []
    while ancien_etat != conf.etat:
        conf.afficher()
        ancien_etat = conf.etat
        conf.evoluer(automate)
    return conf


# Exemple d'utilisation
if __name__ == "__main__":
    # fich, conf =argv[1], argv[2]

    # aut_et_conf = lectureFichier("test/test1.automate", [0,0,0,1,0,0,0])
    test_infini = lectureFichier("test/automate_glider.automate", [0,0,0,1,0,0,0])


    automate = test_infini[0]
    conf = test_infini[1]

    # calculAutomate(automate, conf)
    calculAutomateArret(automate, "000000000000000100000000000000", '1')

