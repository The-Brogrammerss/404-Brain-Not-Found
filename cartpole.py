import gym
import numpy
import BuildNeuralNet
env = gym.make('CartPole-v1')
'''
env.reset()
global fitness
fitness = 0
for x in range(1000):
    env.render()
    action = x % 2
    print(env.action_space)
    observation, reward, done, info = env.step(action)
    fitness += reward
    print("Obv:", observation)
    print("Reward:", fitness)
    if done:
        break
'''

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
        return len(observation), int(x)

def get_fitness(NN):
    observation = env.reset()
    observation = observation.tolist()
    observation.append(1)
    print("observation: " + str(observation))
    fitness = 0
    for x in range(1000):

        NN.predict(observation)
        print(NN.output)
        if round(NN.output[0]) == 1:
            action = 1
        else:
            action = 0
        observation, reward, done, info = env.step(action)
        fitness += reward
        if done:
            print(fitness)
            return fitness
