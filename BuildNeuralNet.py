
class NeuralNet(object):

    def __init__(self, genome):
        self.connections = genome.connections
        self.nodes = genome.nodes
        self.inputLayer = {}
        self.hiddenLayers = {}
        self.outputLayer = {}
        self.output = []
    def buildNeuralNet(self):
        for node in self.nodes:
            if node.type is 'Sensor':
                self.inputLayer[node.nodeNum] = Neuron(t = 'Sensor')
            elif node.type is 'Output':
                self.outputLayer[node.nodeNum] = Neuron(t = 'Output')
            elif node.type is 'Hidden':
                self.hiddenLayers[node.nodeNum] = Neuron(t = 'Hidden')

        for con in self.connections:
            if con.enabled:
                if con.x in self.inputLayer:
                    #print(con.Y)
                    self.inputLayer[con.x].outgoing.append(con.Y)
                    #input node to output node
                    if con.Y in self.outputLayer:
                        self.outputLayer[con.Y].weights[con.x] = con.weight
                    else:
                        self.hiddenLayers[con.Y].weights[con.x] = con.weight
                elif con.x in self.hiddenLayers:
                    self.hiddenLayers[con.x].outgoing.append(con.Y)
                    #input node to output node
                    if con.Y in self.outputLayer:
                        self.outputLayer[con.Y].weights[con.x] = con.weight
                    else:
                        self.hiddenLayers[con.Y].weights[con.x] = con.weight

    def predict(self, inputs):
        for i, keyPair in enumerate(self.inputLayer.items()):
            for Y in keyPair[1].outgoing:
                self.hiddenLayers[Y].incoming[keyPair[0]] = inputs[i]

        calculation = True
        while calculation:
            calculation = False
            for node in self.hiddenLayers:
                if len(self.hiddenLayers[node].incoming) == len(self.hiddenLayers[node].weights):
                    calculation = True
                    theta = sum(self.hiddenLayers[node].incoming[k]*self.hiddenLayers[node].weights[k] for k in self.hiddenLayers[node].incoming)
                    for i in self.hiddenLayers[node].outgoing:
                        if i in self.hiddenLayers:
                            self.hiddenLayers[i].incoming[node] = self.sigmoid(theta)
                        elif i in self.outputLayer:
                            self.outputLayer[i].incoming[node] = self.sigmoid(theta)
                    self.hiddenLayers[node].incoming = {}

        self.output = []
        for x in self.outputLayer:
            theta = sum(self.outputLayer[x].incoming[k]*self.outputLayer[x].weights[k] for k in self.outputLayer[x].incoming)
            self.outputLayer[x].incoming = {}
            self.output.append(self.sigmoid(theta))

    def sigmoid(self, x):
        return x

            #for Y in node.outgoing:

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
