

class Species(object):
    def __init__(self, epochs=0, max_fitness=0, stagnant=0, offspring=0):
        self.epochs_lived = epochs
        self.max_fitness = max_fitness
        self.epochs_stagnant = stagnant
        self.allowed_offspring = offspring

    def __str__(self):
        return ('epochs_lives: {epochs_lived}\n'
                'max_fitness: {max_fitness}\n'
                'epochs_stagnant: {epochs_stagnant}\n'
                'allowed_offspring: {allowed_offspring}\n'
                ).format(**self.__dict__)