


def get_xy():
    return 3, 1

def get_fitness(NN):

    fitness = 0
    _input = [[0,0,1],[1,1,1],[1,0,1],[0,1,1]]
    _output = [0,0,1,1]
    for i, inp in enumerate(_input):
        NN.predict(inp)
        if NN.output[0] == _output[i]:
            fitness += 1

    return fitness
