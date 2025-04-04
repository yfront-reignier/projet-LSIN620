# Variables
PYTHON = python
TESTS = tests.py
MAIN = main.py

# Default target
all: question_1 question_2 question_3 question_4 question_5 question_6 question_7

# Question 1
question_1:
    @echo "Question 1 - Structure de données pour représenter un automate cellulaire :"
    @echo "Classe AutomateCellulaire avec les états et les règles de transition."

# Question 2
question_2:
    @echo "Question 2 - Structure de données pour représenter une configuration :"
    @echo "Classe Configuration avec l'état initial et les méthodes pour évoluer."

# Question 3
question_3:
    @echo "Question 3 - Lecture d'un fichier texte pour initialiser un automate cellulaire."
    $(PYTHON) -m unittest tests.py -k testLectureFichier

# Question 4
question_4:
    @echo "Question 4 - Calcul d'une configuration après un pas de calcul."
    $(PYTHON) $(MAIN) test/automate_30.automate "[0,0,0,1,0,0,0]"

# Question 5
question_5:
    @echo "Question 5 - Simulation d'un automate avec différents modes d'arrêt."
    $(PYTHON) $(MAIN) test/automate_30.automate "000000000000000100000000000000" 1

# Question 6
question_6:
    @echo "Question 6 - Simulation avec affichage de la configuration à chaque pas."
    $(PYTHON) $(MAIN) test/automate_30.automate "000000000000000100000000000000" 2

# Question 7
question_7:
    @echo "Question 7 - Exécution des automates cellulaires intéressants."
    $(PYTHON) $(MAIN) test/automate_glider.automate "[0,0,0,1,0,0,0]"
    $(PYTHON) $(MAIN) test/automate_cycle.automate "[0,1,2,0,1,2,0]"

# Run unit tests
test:
    $(PYTHON) -m unittest $(TESTS)

# Clean up temporary files
clean:
    find . -type f -name "*.pyc" -delete
    find . -type d -name "__pycache__" -exec rm -r {} +

# Help message
help:
    @echo "Available targets:"
    @echo "  all         - Run all questions"
    @echo "  question_1  - Answer to Question 1"
    @echo "  question_2  - Answer to Question 2"
    @echo "  question_3  - Run code for Question 3"
    @echo "  question_4  - Run code for Question 4"
    @echo "  question_5  - Run code for Question 5"
    @echo "  question_6  - Run code for Question 6"
    @echo "  question_7  - Run code for Question 7"
    @echo "  test        - Run all unit tests"
    @echo "  clean       - Remove temporary files"