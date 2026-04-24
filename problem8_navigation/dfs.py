def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    nodes_explored = 0

    while stack:
        node, path = stack.pop()
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get_neighbors(node):
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_explored