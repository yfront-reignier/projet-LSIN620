import unittest
from main import lectureFichier

class Question3(unittest.TestCase):
    def testLectureFichier(self):
        lectureFichier("test/automate.txt")

if __name__ == '__main__':
    unittest.main()
