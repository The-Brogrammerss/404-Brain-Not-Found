class ConnectGenes:

    def __init__(self):
        self.x = None
        self.Y = None
        self.weight = None
        self.enabled = None
        self.innovation = None  # Historical marker

    def __str__(self):
        return ('x: {x}\n'
                'Y: {Y}\n'
                'weight: {weight}\n'
                'enabled: {enabled}\n'
                'innovation: {innovation}'
                ).format(**self.__dict__)
