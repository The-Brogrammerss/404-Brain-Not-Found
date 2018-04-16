import random
import math
# Going off of the Papers structure, a gnome is one


class Genome(object):
    def __init__(self, fitness: int = 0, connections = [], nodes = []):
        self.connections = connections
        self.nodes = nodes
        self.fitness = fitness
        self.adjusted_fitness = 0
        self.other_adjusted_fitness = 0

    def __str__(self):
        result = "fitness: " + str(self.fitness) + '\n'
        result += "Nodes in Genome:\n"
        for node in self.nodes:
            result += str(node) + '\n'

        result += "Connections details:\n"
        for connect in self.connections:
            result += str(connect) + '\n\n'

        return result
