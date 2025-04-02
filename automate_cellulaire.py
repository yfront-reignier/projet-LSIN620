import numpy as np

class AutomateCellulaire:
    def __init__(self, etats, transitions):
        self.etats = etats
        self.transitions = transitions
        self.configurations = [self.etats]

    def __repr__(self):
        return set(self.transitions)
