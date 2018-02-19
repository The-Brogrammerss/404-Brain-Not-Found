class NodeGenes(object):

    def __init__(self):
        self.nodeNum = None
        self.type = None #Sensor, Hidden, Output

    def __str__(self):
        return ('nodeNum: {nodeNum}\n'
                'type: {type}\n'
                ).format(**self.__dict__)
