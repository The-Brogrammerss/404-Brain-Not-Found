import unittest
from Population import Population
from ConnectGenes import ConnectGenes
from Genome import Genome
from Config import Config

class test_population(unittest.TestCase):

    # def setUp(self):
    pop_obj = Population([])
    next_gen = Population([])
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

    gnome.connections.append(cons)
    pop_obj.currentPop.append(gnome)

    def test_add_node(self):
        print(self.pop_obj.connectionList[0])
        self.next_gen.mutate_add_node(self.pop_obj.currentPop[0])
        print(self.next_gen.connectionList[0])
