import heapq

def a_star(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current == goal:
            return path, g

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

path, cost = a_star(graph, heuristic, 'A', 'D')

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)