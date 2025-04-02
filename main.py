from automate_cellulaire import AutomateCellulaire

def lectureFichier(fichier, initial):
    conf = recupConf(fichier)
    automate = AutomateCellulaire(initial, conf)

    return automate

def recupConf(fichier):
    configuration = {}
    with open(fichier, 'r') as f:
        for ligne in f:
            if ligne[0] not in ["0", "1", "2", "3"]:
                continue
            part_ligne = ligne.split('->')
            transitions = tuple(map(int, part_ligne[0].split(' ')))
            nouv_etat = int(part_ligne[1][0])
            configuration[transitions] = nouv_etat
    return configuration

def calculAutomate(automate, configuration):
    conf_final = configuration

    return conf_final


if __name__ == '__main__':
    lectureFichier("test/automate.txt")