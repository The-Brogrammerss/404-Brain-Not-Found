class ConnectGene(object):

    def __init__(self, x=None, Y=None, weight=None, enabled=None, innovation=None, pair = None):
        self.x = x
        self.Y = Y
        self.weight = weight
        self.enabled = enabled
        self.innovation = innovation  # Historical marker
        self.pairNumber = pair

    def __str__(self):
        return ('x: {x}\n'
                'Y: {Y}\n'
                'weight: {weight}\n'
                'enabled: {enabled}\n'
                'innovation: {innovation}\n'
                'pair: {pairNumber}'
                ).format(**self.__dict__)
