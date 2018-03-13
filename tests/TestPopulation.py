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

        self.next_gen.mutate_add_node(self.pop_obj.currentPop[0])

        self.assertEqual(self.next_gen.connectionList[1].x, 1)
        self.assertEqual(self.next_gen.connectionList[1].Y, 3)
        self.assertEqual(self.next_gen.connectionList[1].enabled, True)
        self.assertEqual(self.next_gen.connectionList[1].weight, 100)
        self.assertEqual(self.next_gen.innovationCounter, 3)

        self.assertEqual(self.next_gen.connectionList[2].x, 3)
        self.assertEqual(self.next_gen.connectionList[2].Y, 2)
        self.assertEqual(self.next_gen.connectionList[2].enabled, True)

    def test_existing_connection(self):
        Population.x = 1
        Population.Y = 2
        cons2 = ConnectGenes()
        cons2.x = 1
        cons2.Y = 3
        cons2.innovation = 2
        cons2.weight = 10
        cons2.enabled = True
        self.gnome.connections.append(cons2)

        cons3 = ConnectGenes()
        cons3.x = 1
        cons3.Y = 3
        cons3.innovation = 3
        cons3.weight = 10
        cons3.enabled = True

        self.gnome.connections.append(cons3)
        self.next_gen.innovationCounter = 3
        self.next_gen.mutate_add_node(self.pop_obj.currentPop[0])

        print(self.next_gen.currentPop[0].connections[0])
        print(self.next_gen.currentPop[0].connections[1])
        print(self.next_gen.currentPop[0].connections[2])

        self.assertEqual(self.next_gen.currentPop[0].connections[0].x, 1)
        self.assertEqual(self.next_gen.currentPop[0].connections[0].Y, 2)
        self.assertEqual(self.next_gen.currentPop[0].connections[0].enabled, False)

        self.assertEqual(self.next_gen.currentPop[0].connections[1].x, 1)
        self.assertEqual(self.next_gen.currentPop[0].connections[1].Y, 3)
        self.assertEqual(self.next_gen.currentPop[0].connections[1].enabled, True)
        self.assertEqual(self.next_gen.currentPop[0].connections[1].weight, 100)

        self.assertEqual(self.next_gen.currentPop[0].connections[2].x, 3)
        self.assertEqual(self.next_gen.currentPop[0].connections[2].Y, 2)
        self.assertEqual(self.next_gen.currentPop[0].connections[2].enabled, True)







