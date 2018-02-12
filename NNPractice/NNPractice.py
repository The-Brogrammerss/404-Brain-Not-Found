import math
import numpy as np
class Neural_Net:

    def __init__(self, layers):
        self.weights = []
        for i in range(1, len(layers) - 1):
            rand_weights = 2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1
            self.weights.append(rand_weights)
        r = 2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1
        self.weights.append(r)

    def sigmoid(z, derive):
        if (derive == True):
            return z * (1 - z)
        vz = np.array(z)
        g = 1.0 / (1.0 + np.exp(-vz));
        return g;

    def train(self, X, y, alpha = .2, epochs=100):
        # adds bias to input from
        # http://www.bogotobogo.com/python/python_Neural_Networks_Backpropagation_for_XOR_using_one_hidden_layer.php
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)

        #theta0 = 2 * np.random.random((3, 1)) - 1  # 3x1 array of random weights from 0 to 1
        for blah in range(epochs):
            theta0 = np.random.randint(X.shape[0])
            a1 = [X[theta0]]
            print(a1)
            for bleh in range(len(self.weights)):
                dotty = np.dot(a1[1], self.weights[1])
                activ_lay = Neural_Net.sigmoid(dotty, False)
                a1.append(activ_lay)

if '__main__' == __name__:
    nn = Neural_Net([2, 2, 1])
    X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]) #input layer
    y = np.array([[0, 1, 1, 0]]).T #correct dataset
    Neural_Net.train(X, y)
