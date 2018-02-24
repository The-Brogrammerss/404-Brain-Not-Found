class ConnectGenes(object):

    def __init__(self, x: object = None, Y: object = None, weight: object = None, enabled: object = None, innovation: object = None) -> object:
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
