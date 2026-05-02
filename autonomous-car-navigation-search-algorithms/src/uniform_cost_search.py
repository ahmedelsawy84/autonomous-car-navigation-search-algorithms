import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost


def uniform_cost_search(graph, start, goal):
    frontier = [Node(start)]
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        if node.state == goal:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1]

        explored.add(node.state)
        for cost, result_state in graph[node.state]:
            if result_state not in explored:
                heapq.heappush(frontier, Node(result_state, node, node.path_cost + cost))


def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        # Look up the cost between consecutive nodes in the path
        for cost, neighbor in graph[path[i]]:
            if neighbor == path[i + 1]:  # Find the cost from path[i] to path[i+1]
                total_cost += cost
                break  # Once we find the cost for the edge, stop looking further
    return total_cost


def visualize_graph(graph, path=None):
    G = nx.DiGraph()
    labels = {(node, child): cost for node, edges in graph.items() for cost, child in edges}
    for node, edges in graph.items():
        for cost, child in edges:
            G.add_edge(node, child, weight=cost)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=3000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    if path:
        nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i + 1]) for i in range(len(path) - 1)],
                               edge_color='blue', width=1)
    plt.show()

# Define the graph as an adjacency list
graph = {
         'tagmoa': [(15, 'nasrcity'), (19, 'sheraton')],
         'nasrcity': [(22, 'maadi')],
         'maadi': [(24, 'korba'), (27, 'elhegaz')],
         'sheraton': [(7,'korba'),(10,'maryland')],
         'korba': [(7, 'nasrcity')],
         'maryland': [(2, 'elhegaz')],
         'elhegaz': []}

start, goal = 'tagmoa', 'elhegaz'

# Run uniform cost search
path = uniform_cost_search(graph, start, goal)

# Visualize the graph and the path
visualize_graph(graph, path)

# Calculate and print the total cost of the path
total_cost = calculate_path_cost(graph, path)
print("Path from", start, "to", goal, ":", path)
print("Total cost of the path:", total_cost," km ")