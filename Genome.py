import random
import math
# Going off of the Papers structure, a gnome is one


class Genome(object):
    def __init__(self, fitness: int = 0, connections = [], nodes = []):
        self.connections = connections
        self.nodes = nodes
        self.fitness = fitness

    def __str__(self):
        result = "fitness: " + str(self.fitness) + '\n'
        result += "Nodes in Genome:\n"
        for node in self.nodes:
            result += str(node) + '\n'

        result += "Connections details:\n"
        for connect in self.connections:
            result += str(connect) + '\n\n'

        return result

    def mutate_weight(self):
        perturb_rate = 0.9
        perturb_chance = random.random()
        random_connection = random.randint(0, len(self.connections) -1)
        if perturb_chance <= perturb_rate:
            self.connections[random_connection].weight = round(self.connections[random_connection].weight * random.uniform(0.8, 1.2))

        else:
            self.connections[random_connection].weight = random.randrange(-100, 100, 1)

    def add_node(self):
        random_connection = random.randint(0, len(self.connections) - 1)
        Y = self.connections[random_connection].Y
        x = self.connections[random_connection].x
        weight = self.connections[random_connection].weight

