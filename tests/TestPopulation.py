import unittest
from Population import Population
from ConnectGenes import ConnectGenes
from Genome import Genome
from Config import Config
import copy

class test_population(unittest.TestCase):

    # def setUp(self):
    pop_obj = Population([])
    gnome = Genome()
    cons = ConnectGenes()

    cons.x = 1
    cons.Y = 2
    cons.innovation = 1
    cons.weight = 10
    cons.enabled = True
    config = Config()

    pop_obj.connectionList.append(cons)
    pop_obj.innovationCounter = 1
    pop_obj.maxNodes = 2

    gnome.connections.append(cons)
    pop_obj.currentPop.append(gnome)
    next_gen = copy.deepcopy(pop_obj)
    next_gen.currentPop = []

    def test_add_node(self):
        print(self.pop_obj.connectionList[0])
        self.next_gen.mutate_add_node(self.pop_obj.currentPop[0])
        print(self.next_gen.connectionList[1])
        print(self.next_gen.connectionList[2])
