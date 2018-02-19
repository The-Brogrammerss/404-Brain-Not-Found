
class NeuralNet(object):

    def __init__(self, genome):
        self.connections = genome.connections
        self.nodes = genome.nodes
        self.inputLayer = {}
        self.hiddenLayers = [{}]
        self.outputLayer = {}

    def buildNeuralNet(self):
        for node in self.nodes:
            if node.type is 'Sensor':
                self.inputLayer[node.nodeNum] = Neuron(t = 'Sensor')
            elif node.type is 'Output':
                self.outputLayer[node.nodeNum] = Neuron(t = 'Output')

        leftOverCon = []

        #Build first hidden layer if one exists
        for con in self.connections:
            #Check for all input layer connections
            if con.x in self.inputLayer:
                #Check if output is in output layer
                if con.Y not in self.outputLayer:
                    self.hiddenLayers[0][con.Y] = Neuron(t = 'Hidden')
                    if con.enabled is True:
                        self.hiddenLayers[0][con.Y].weights[con.x] = con.weight
                        self.inputLayer[con.x].outgoing.append(con.Y)
                #Connection is input layer to output layer
                else:
                    if con.enabled is True:
                        self.outputLayer[con.Y].weights[con.x] = con.weight
                        self.inputLayer[con.x].outgoing.append(con.Y)
            #connection is hidden layer to hidden layer
            else:
                leftOverCon.append(con)






class Neuron(object):

    def __init__(self , t):
        self.incoming = {}
        self.weights = {}
        self.outgoing = []
        self.type = t

    def __str__(self):
        return('incoming: {incoming}\n'
               'weights: {weights}\n'
               'outgoing: {outgoing}\n'
               'type: {type}\n'
               ).format(**self.__dict__)
