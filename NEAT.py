from ConnectGenes import ConnectGenes
from Genome import Genome
from NodeGenes import NodeGenes
from cartpole import CartPole
import cartpole

popCap = 200
pop = []

# os.system("cartpole.py")
numInputs, numY = CartPole.getXy()
numY = int(numY)
print("num ouputs:", numY)
print("num Inputs:", numInputs)

for gnum in range(popCap):
    gnome = Genome()
    cons = ConnectGenes()
    nodes = NodeGenes()

    for i in range(numInputs + 1):
        nodes.nodeNum = i
        nodes.type = "Sensor"
    for i in range(numY):



