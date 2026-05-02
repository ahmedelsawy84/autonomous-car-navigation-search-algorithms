import networkx as nx
import matplotlib.pyplot as plt
import heapq
pos1={
    "tagmoa":(1,5),
    "nasrcity":(7.6,6.6),
    "maadi":(1.6,2.4),
    "sheraton":(6.0,3.8),
    "korba":(7.9,3.6),
    "maryland":(4.1,8.4),
    "elhegaz":(3.3,6.5)
}


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

        explored.add(node.state) #mark the current as explored
        for cost, result_state in graph[node.state]: #traverse children (neighbors) then select node with the least cost and name it result_state
            if result_state not in explored:
                heapq.heappush(frontier, Node(result_state, node, node.path_cost + cost))  #add result_state to the queue with the updated path_cost
#result_state= chosen node,node=parent of the chosen node,cost=updated cost

def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        # -1 because the last node does not have a child
        for cost, neighbor in graph[path[i]]:#current node = path[i] the loop moves to see all the children  of the current node which consists of the cost and the name of this child
            if neighbor == path[i + 1]:  # Find the cost from path[i] to path[i+1]
                total_cost += cost
                break
    return total_cost


def visualize_graph(graph, path=None):
    G = nx.DiGraph()
    labels = {(node, child): cost for node, edges in graph.items() for cost, child in edges}#dict named labels (node,child)are the keys to move the cost from node to child
    for node, edges in graph.items():
        for cost, child in edges:
            G.add_edge(node, child, weight=cost)

    nx.draw(G, pos=pos1, with_labels=True, node_color='lightgreen', node_size=2000,font_weight='bold')#draw nodes
    nx.draw_networkx_edge_labels(G, pos=pos1, edge_labels=labels, font_weight='bold',font_size=12)#draw edges
    plt.margins(0.007)
    if path:
        #highlight the path
        nx.draw_networkx_edges(G, pos=pos1, edgelist=[(path[i], path[i + 1]) for i in range(len(path) - 1)], edge_color='blue', width=1)
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