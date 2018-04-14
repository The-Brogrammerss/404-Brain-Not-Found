

class Species(object):
    def __init__(self, epochs=0, max_fitness=0, stagnant=0):
        self.epochs_lived = epochs
        self.max_fitness = max_fitness
        self.epochs_stagnant = stagnant
