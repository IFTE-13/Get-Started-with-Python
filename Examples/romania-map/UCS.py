import queue

def uniform_cost_search(graph, start, end):
    if start not in graph:
        raise ValueError(f"{start} not found in graph!")
    if end not in graph:
        raise ValueError(f"{end} not found in graph!")

    frontier = queue.PriorityQueue()
    frontier.put((0, [start]))  # (cost, path)
    explored = set()

    while not frontier.empty():
        cost, path = frontier.get()
        current = path[-1]

        if current == end:
            print(f"Path found: {path}, Cost = {cost}")
            return path, cost

        if current in explored:
            continue

        explored.add(current)

        for neighbor, edge_cost in graph[current].items():
            if neighbor not in explored:
                new_path = path + [neighbor]
                frontier.put((cost + edge_cost, new_path))

    print("No path found!")
    return None, None


def read_graph():
    """
    Input format:
    First line: number of nodes
    Next lines: node neighbor1 cost1 neighbor2 cost2 ...
    Example:
    3
    A B 5 C 10
    B A 5 C 3
    C A 10 B 3
    """
    lines = int(input("Number of nodes: "))
    graph = {}

    for _ in range(lines):
        tokens = input().split()
        node = tokens[0]
        graph[node] = {}
        for i in range(1, len(tokens) - 1, 2):
            neighbor = tokens[i]
            cost = int(tokens[i + 1])
            graph[node][neighbor] = cost
    return graph


def main():
    graph = read_graph()
    uniform_cost_search(graph, 'Arad', 'Bucharest')


if __name__ == "__main__":
    main()
