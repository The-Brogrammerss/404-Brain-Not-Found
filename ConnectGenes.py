

class ConnectGenes:

    def __init__(self):
        self.x = None
        self.Y = None
        self.weight = None
        self.status = None
        self.innovation = None

    def __str__(self):
        return ('x: {x}\n'
                'Y: {Y}\n'
                'weight: {weight}\n'
                'status: {status}\n'
                'innovation: {innovation}'
                ).format(**self.__dict__)


if __name__ == '__main__':
    a = ConnectGenes()
    print (a)