from NodeGenes import NodeGenes
from ConnectGenes import ConnectGenes
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

#Test if __str__ works
# if '__main__' == __name__:
#     g = Genome()
#
#     for i in range(4):
#         n = NodeGenes()
#         c = ConnectGenes()
#         n.nodeNum = i
#         c.innovation = i
#         g.nodes.append(n)
#         g.connections.append(c)
#     print(g)
