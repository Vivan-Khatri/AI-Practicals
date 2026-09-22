from collections import deque

# Graph
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

# BFS
def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# DFS
def dfs(start):
    visited = set()
    stack = [start]

    result = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            # Reverse so traversal order matches graph order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# Main
start = 0

print("BFS:", bfs(start))
print("DFS:", dfs(start))
