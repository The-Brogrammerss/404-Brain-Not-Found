import math


class NeuralNet(object):


    def __init__(self, genome):
        self.connections = genome.connections
        self.nodes = genome.nodes
        self.inputLayer = {}
        self.hiddenLayers = {}
        self.outputLayer = {}
        self.output = []

    def __str__(self):
        s = ""
        for key, value in self.inputLayer.items():
            s += (str(key) + ': ' + str(value) + '\n')
        for key, value in self.outputLayer.items():
            s += (str(key) + ': ' + str(value) + '\n')
        return s

    def build_neural_net(self):
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
        if len(self.hiddenLayers) > 0:
            for i, keyPair in enumerate(self.inputLayer.items()):
                for Y in keyPair[1].outgoing:
                    if Y in self.hiddenLayers:
                        self.hiddenLayers[Y].incoming[keyPair[0]] = inputs[i]
                    elif Y in self.outputLayer:
                        self.outputLayer[Y].incoming[keyPair[0]] = inputs[i]
            calculation = True
        else:
            calculation = False

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

        for node in self.inputLayer:
            for i in self.inputLayer[node].outgoing:
                if i in self.outputLayer:
                    self.outputLayer[i].incoming[node] = inputs[node-1]

        self.output = []
        for x in self.outputLayer:
            theta = sum(self.outputLayer[x].incoming[k]*self.outputLayer[x].weights[k] for k in self.outputLayer[x].incoming)
            self.outputLayer[x].incoming = {}
            self.output.append(self.sigmoid(theta))

    def sigmoid(self, x):
        if x < 0:
            return 1 - 1 / (1 + math.exp(x))
        else:
            return 1 / (1 + math.exp(-x))
        # return (1 / (1 + math.exp(-4.9 * x)))


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
