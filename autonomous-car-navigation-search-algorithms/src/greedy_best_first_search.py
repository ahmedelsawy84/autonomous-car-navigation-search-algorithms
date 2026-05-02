import heapq


def greedy_best_first_search(graph, start, goal, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    visited = set()
    parent = {start: None}  # To reconstruct the path

    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return reversed path

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    parent[neighbor] = current
                    heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return "Goal not reachable"


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 1,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'
result = greedy_best_first_search(graph, start, goal, heuristic)
print(result)