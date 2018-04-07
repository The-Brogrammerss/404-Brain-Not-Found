class NodeGene(object):

    def __init__(self, nodeNum = None, t = None, layer = None):
        self.nodeNum = nodeNum
        self.type = t #Sensor, Hidden, Output
        self.layer = layer

    def __str__(self):
        return ('nodeNum: {nodeNum}\n'
                'type: {type}\n'
                'layer: {layer}\n'
                ).format(**self.__dict__)
