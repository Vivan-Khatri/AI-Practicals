import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float("inf")


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}

path, cost = a_star(graph, heuristic, 'A', 'G')

print("Path:", path)
print("Cost:", cost)
