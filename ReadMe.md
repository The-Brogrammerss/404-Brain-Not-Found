To run the program you will need python and gym from https://gym.openai.com/docs/

python ./NEAT.py

There are some config settings inside of NEAT.py __main__ for changing the game and what the fitness level needs to be. Some other parameters that can be changed are population size (popCap) and epochs. Epochs can be changed by the main loop of the program in __main__.

The project does not utilize the GPU and is overall not very quick or efficient. The main idea was to use as few libraries as possible and to recreate what was described in this paper http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf with some of our own interpretations. 

Gym
- pip install gym
