import heapq

# -----------------------------
# Romania Map
# -----------------------------
graph = {
    "Arad": {"Timisoara": 118, "Sibiu": 140, "Zerind": 75},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu": 80},
    "Sibiu": {"Arad": 140, "Oradea": 151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

heuristicSLD = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242,
    "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
    "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesi": 100, "RimnicuVilcea": 193,
    "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199,
    "Zerind": 374
}

# -----------------------------
# Node Class
# -----------------------------
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, problem):
        return [Node(next_state, self, action,
                     problem.path_cost(self.path_cost, self.state, action, next_state))
                for action, next_state in problem.graph[self.state].items()]

    def solution(self):
        node, path = self, []
        while node:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))


# -----------------------------
# Graph Problem Class
# -----------------------------
class GraphProblem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + self.graph[state1][state2]


# -----------------------------
# General Graph Search
# -----------------------------
def graph_search(problem, f):
    frontier = []
    heapq.heappush(frontier, (f(Node(problem.initial)), Node(problem.initial)))
    explored = set()

    while frontier:
        _, node = heapq.heappop(frontier)
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored:
                heapq.heappush(frontier, (f(child), child))
    return None


# -----------------------------
# Search Algorithms
# -----------------------------
def uniform_cost_search(problem):
    return graph_search(problem, lambda node: node.path_cost)

def GBFS(problem):
    return graph_search(problem, lambda node: heuristicSLD[node.state])

def A_star_search(problem):
    return graph_search(problem, lambda node: node.path_cost + heuristicSLD[node.state])


# -----------------------------
# Run the Algorithms
# -----------------------------
gp = GraphProblem("Arad", "Bucharest", graph)

print("---------- UCS ----------")
goalNode = uniform_cost_search(gp)
print("Path:", goalNode.solution())
print("Cost:", goalNode.path_cost)

print("\n---------- GBFS ----------")
goalNode = GBFS(gp)
print("Path:", goalNode.solution())
print("Cost:", goalNode.path_cost)

print("\n---------- A* Search ----------")
goalNode = A_star_search(gp)
print("Path:", goalNode.solution())
print("Cost:", goalNode.path_cost)
