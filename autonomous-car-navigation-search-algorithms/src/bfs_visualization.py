import random
import networkx as nx  # NetworkX is a Python package for the creation, manipulation, and study of complex networks
import matplotlib.pyplot as plt


def bfs(graph, start, goal=None):
    visited = []
    queue = [start]
    result = []

    while queue:
        vertex = queue.pop(0)  # Dequeue the first element
        if vertex not in visited:  # If the vertex has not been visited
            visited.append(vertex)  # Mark the vertex as visited
            result.append(vertex)  # Add the vertex to the result list
            print(f"Visited: {visited}, Queue: {queue}")
            if vertex == goal:  # If the goal node is reached
                print(f"Reached goal node: {goal}")
                break  # Exit the loop
            for neighbor in graph[vertex]:  # Add the neighbors of the vertex to the queue
                if neighbor not in visited and neighbor not in queue:  # If the neighbor has not been visited or is not in the queue
                    queue.append(neighbor)  # Add the neighbor to the queue
                    print(f"Added {neighbor} to queue, New Queue: {queue}")

    return result


def generate_random_tree(num_nodes):
    if num_nodes == 0:  # If the number of nodes is 0, return an empty dictionary
        return {}

    graph = {i: [] for i in
             range(num_nodes)}  # Create a dictionary with keys from 0 to num_nodes-1 and empty lists as values
    for i in range(1, num_nodes):  # Iterate from 1 to num_nodes-1
        parent = random.randint(0, i - 1)  # Generate a random parent node
        graph[parent].append(i)  # Add the child node to the parent node
        graph[i].append(parent)  # Add the parent node to the child node

    return graph


'''-------------------------------------------------------------------------------------------------------------------------------------'''
num_nodes = 10  # Number of nodes in the tree
graph = generate_random_tree(num_nodes)  # Generate a random tree
start_node = 0  # Start node
goal_node = None  # Goal node
print("Generated graph:", graph)  # Print the generated graph
print("BFS traversal:", bfs(graph, start_node, goal_node))  # Perform BFS traversal of the graph


# Draw Graph
def draw_graph(graph, visited=None, step=0):
    G = nx.Graph()  # Create a new graph
    for node, neighbors in graph.items():  # Iterate over the nodes and neighbors of the graph
        for neighbor in neighbors:  # Iterate over the neighbors of the node
            G.add_edge(node, neighbor)  # Add an edge between the node and the neighbor

    pos = nx.spring_layout(G)  # Compute the spring layout, which is the positioning of the nodes
    node_colors = ['lightblue' if node not in visited else 'Red' for node in G.nodes()]  # Set the node colors
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=500, font_size=10)
    plt.title(f'Step {step}')
    plt.savefig(f'step_{step}.png')
    plt.show()


'''-------------------------------------------------------------------------------------------------------------------'''
visited_nodes = []
step = 0
for node in bfs(graph, start_node, goal_node):  # Perform BFS traversal of the graph
    visited_nodes.append(node)  # Add the visited node to the list of visited nodes
    draw_graph(graph, visited=visited_nodes, step=step)  # Draw the graph with the visited nodes
    step += 1


