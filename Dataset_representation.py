import networkx as nx
from dotenv.main import load_dotenv
import os
import matplotlib.pyplot as plt
import numpy as np

# Read data from the CSV file
load_dotenv()
csv_file_path = os.environ['CSV_FILE_PATH']
with open(csv_file_path,'r') as file:
    lines = file.readlines()

#Create a graph
G = nx.Graph()

# Add edges based on the data
for line in lines:
    source, target = line.strip().split(',')  # Split by commas
    G.add_edge(source, target)

# The below code is to display the whole data as a graph

# # Draw the graph
# pos = nx.spring_layout(G)  # Position nodes using a spring layout
# nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_color="black")
# plt.show()



# The below code is for representing the whole graph as an adjacency matrix

# Get a list of nodes in the graph
nodes = list(G.nodes())

# Create an adjacency matrix
adjacency_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)

# Fill in the adjacency matrix based on the edges in the graph
for source, target in G.edges():
    source_index = nodes.index(source)
    target_index = nodes.index(target)
    adjacency_matrix[source_index, target_index] = 1
    adjacency_matrix[target_index, source_index] = 1  # Graph is undirected

for row in adjacency_matrix:
    print(row)