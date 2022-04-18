# to implement dijkstra's algorithm, 3 hash tables must be used: graph, costs, parents

# create graph hash table:
graph = {}
graph["start"] = {} 
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# create costs hash table:
# (the cost of a node is how long it takes to get to that node from the start)
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# create parents hash table:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# create an array to keep track of all the processed nodes
# (nodes don't need to be processed more than once)
processed = []

# define "find_lowest_cost_node()" function:
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# dijkstra's algorithm:
node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
