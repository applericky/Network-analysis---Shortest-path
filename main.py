import networkx
import matplotlib.pyplot as plot

routers = range(1, 5)
trunks = [(5, 1), (2, 4), (3, 1)]
network = networkx.Graph()
network.add_nodes_from(routers)
networkx.draw(network)
