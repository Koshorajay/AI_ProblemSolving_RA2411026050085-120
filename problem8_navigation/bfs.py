from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    nodes_explored = 0

    while queue:
        node, path = queue.popleft()
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get_neighbors(node):
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_explored