
# Graph representation (node: [(neighbor, cost)])
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values (h(n))
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 4,
    'F': 2,
    'G': 0
}

def a_star(start, goal):
    open_list = [start]        # nodes to explore
    closed_list = []           # explored nodes

    g_cost = {start: 0}        # distance from start
    parent = {start: None}     # to track path

    while open_list:
        # find node with lowest f(n) = g(n) + h(n)
        current = min(open_list, key=lambda node: g_cost[node] + heuristic[node])

        # if goal reached
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g_cost[goal]

        open_list.remove(current)
        closed_list.append(current)

        # explore neighbors
        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            new_g = g_cost[current] + cost

            # if new node OR better path found
            if neighbor not in open_list:
                open_list.append(neighbor)
            elif new_g >= g_cost.get(neighbor, float('inf')):
                continue

            # update values
            parent[neighbor] = current
            g_cost[neighbor] = new_g

    return None, float('inf')

start_node = 'B'
goal_node = 'G'

path, cost = a_star(start_node, goal_node)

if path:
    print("SUCCESS!! Path found.")
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")