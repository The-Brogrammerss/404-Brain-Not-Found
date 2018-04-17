import gym

from BuildNeuralNet import NeuralNet

env = gym.make('MountainCar-v0')

def get_xy():
    env.reset()
    for x in range(1000):
        action = x % 2
        observation, reward, done, info = env.step(action)
        x = str(env.action_space)
        x = (x[9]) # action space returns 'Discrete(#)' and we just want the #
        return len(observation) + 1, x

def get_fitness(NN):
    observation = env.reset()
    observation = observation.tolist()
    fitness = 0
    for x in range(10000):
        observation.append(1)
        NN.predict(observation)
        nno = NN.output
        choice = nno.index(max(nno)) # index of max numbers first instance
        observation, reward, done, info = env.step(round(choice))
        if type(observation) is not list:
            observation = observation.tolist()
        fitness += reward
        if done:
            return fitness


def render_game(gnome):
    env = gym.make('MountainCar-v0')
    NN = NeuralNet(gnome)
    NN.build_neural_net()
    observation = env.reset()
    observation = observation.tolist()
    observation.append(1)
    fitness = 0

    for x in range(10000):
        NN.predict(observation)
        nno = NN.output
        choice = nno.index(max(nno)) # index of max numbers first instance
        observation, reward, done, info = env.step(round(choice))
        env.render()
        observation = observation.tolist()
        observation.append(1)
        fitness += reward
        if done:
            break
