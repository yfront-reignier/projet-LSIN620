import unittest
from main import lectureFichier, calculAutomate, calculAutomateArret
from automate_cellulaire import AutomateCellulaire
from configuration import Configuration

class Question3(unittest.TestCase):
    def testLectureFichier(self):
        automate, conf = lectureFichier("test/automate_30.automate", [0, 0, 0, 1, 0, 0, 0])
        self.assertIsInstance(automate, AutomateCellulaire)
        self.assertIsInstance(conf, Configuration)

class Question4(unittest.TestCase):
    def testCalculAutomate(self):
        automate, conf = lectureFichier("test/automate_110.automate", [0, 0, 0, 1, 0, 0, 0])
        calculAutomate(automate, conf)
        self.assertIsNotNone(conf.etat)

class Question5(unittest.TestCase):
    def testCalculAutomateArret(self):
        automate, conf = lectureFichier("test/automate_110.automate", [0, 0, 0, 1, 0, 0, 0])
        calculAutomateArret(automate, "000010000", '1', 10, [])
        self.assertIsNotNone(conf.etat)

        calculAutomateArret(automate, "000010000", '2', 10, [1, 1, 1, 1, 1, 0, 0, 0, 0])
        self.assertIsNotNone(conf.etat)

        calculAutomateArret(automate, "010000000", '3', 10, [1, 0, 1, 1, 1, 0, 0, 0, 0])
        self.assertIsNotNone(conf.etat)

if __name__ == '__main__':
    unittest.main()
