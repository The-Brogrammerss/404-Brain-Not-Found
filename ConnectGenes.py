class ConnectGenes(object):

    def __init__(self, x = None, Y = None, weight = None, enabled = None, innovation = None):
        self.x = x
        self.Y = Y
        self.weight = weight
        self.enabled = enabled
        self.innovation = innovation  # Historical marker

    def __str__(self):
        return ('x: {x}\n'
                'Y: {Y}\n'
                'weight: {weight}\n'
                'enabled: {enabled}\n'
                'innovation: {innovation}'
                ).format(**self.__dict__)
