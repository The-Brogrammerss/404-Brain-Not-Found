class NodeGenes(object):

    def __init__(self, nodeNum = None, t = None):
        self.nodeNum = nodeNum
        self.type = t #Sensor, Hidden, Output

    def __str__(self):
        return ('nodeNum: {nodeNum}\n'
                'type: {type}\n'
                ).format(**self.__dict__)
