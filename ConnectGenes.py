

class ConnectGenes:

    def __init__(self):
        self.x = None
        self.Y = None
        self.weight = None
        self.status = None
        self.innovation = None

    def __str__(self):
        return "x:", self.x + "Y:", self.Y, "weight:", self.weight, "status:", self.status, "innovation:", self.innovation

