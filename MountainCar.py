import gym

from BuildNeuralNet import NeuralNet

env = gym.make('MountainCar-v0')

def get_xy():
    env.reset()
    for x in range(1000):
        #env.render()
        #action = x % 2
        # print("action space: ", env.action_space)
        action = x % 2
        observation, reward, done, info = env.step(action)
        #fitness += reward
        # print("Obv:", observation)
        #print("Reward:", fitness)
        x = str(env.action_space)
        x = (x[9]) # action space returns 'Discrete(#)' and we just want the #
        return len(observation) + 1, 3

def get_fitness(NN):
    observation = env.reset()
    observation = observation.tolist()
    observation.append(1)
    # print("observation: " + str(observation))
    fitness = 0
    for x in range(10000):
        NN.predict(observation)
        for index in range(3):
            NN.output[index] = round(NN.output[index])

        nno = NN.output
        # print("output from nn:", NN.output[0])
        if nno[0] == 1 and nno[1] == 1:
            # print("pick me!!!!!!!!!!!!!\n")
            observation, reward, done, info = env.step(0)
            # return fitness
        elif nno[0] == 1 and nno[2] == 1:
            # print("pick me!!!!!!!!!!!!!\n")
            observation, reward, done, info = env.step(0)
            # return fitness
        elif nno[1] == 1 and nno[2] == 1:
            # print("pick me!!!!!!!!!!!!!\n")
            observation, reward, done, info = env.step(0)
            # return fitness
        elif nno[0] == 0 and nno[1] == 0 and nno[2] == 0:
            # print("pick me!!!!!!!!!!!!!\n")
            observation, reward, done, info = env.step(0)
            # return fitness
        else:
            for index in range(3):
                if nno[index] == 1:
                    # print(index)
                    # print("no me*************\n")
                    observation, reward, done, info = env.step(index)
        if type(observation) is not list:
            observation = observation.tolist()
        observation.append(1)
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
    # print("observation: " + str(observation))
    fitness = 0

    for x in range(10000):

        NN.predict(observation)
        observation, reward, done, info = env.step(round(NN.output[0]))
        env.render()
        observation = observation.tolist()
        observation.append(1)
        fitness += reward
        if done:
            break