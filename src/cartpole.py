import gym
from src.BuildNeuralNet import NeuralNet
env = gym.make('CartPole-v1')

def get_xy():
    env.reset()
    for x in range(1000):
        #env.render()
        #action = x % 2
        #print(env.action_space)
        action = x % 2
        observation, reward, done, info = env.step(action)
        #fitness += reward
        #print("Obv:", observation)
        #print("Reward:", fitness)
        x = str(env.action_space)
        x = (x[9]) # action space returns 'Discrete(#)' and we just want the #
        return len(observation) + 1, 1

def get_fitness(NN):
    observation = env.reset()
    observation = observation.tolist()
    observation.append(1)
    # print("observation: " + str(observation))
    fitness = 0
    for x in range(10000):

        NN.predict(observation)
        observation, reward, done, info = env.step(round(NN.output[0]))
        observation = observation.tolist()
        observation.append(1)
        fitness += reward
        if done:
            # print(fitness)
            return fitness

def render_game(gnome):
    print(gnome.fitness)
    env = gym.make('CartPole-v1')
    NN = NeuralNet(gnome)
    NN.build_neural_net()

    observation = env.reset()
    observation = observation.tolist()
    observation.append(1)
    print("observation: " + str(observation))
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
