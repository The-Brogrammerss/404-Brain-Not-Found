class Population(object):

    def __init__(self, pop):
        self.currentPop = pop
        self.innovationCounter = 0
        self.connectionList = []
        self.maxNodes = 0


    def crossbreed(self):
        parents = self.currentPop
        self.currentPop = []
        
