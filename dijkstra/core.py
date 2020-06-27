def dijkstra(graph: list, start: int) -> dict:
    """ TODO
    """
    distances = dict()
    predecessors = dict()
    quantity = set()

    initialize(graph, start, distances, predecessors, quantity)
    while len(quantity) != 0:
        u = find_smallest_distance(quantity, distances)
        if u in quantity:
            quantity.remove(u)
        else:
            print("Unable to remove u from list.")

        neighbours = set()
        for connection in graph:
            if connection[0] == u:
                neighbours.add(connection[1])

        for v in neighbours:
            if v in quantity:
                update_distance(graph, u, v, distances, predecessors)
        
    return predecessors

def initialize(graph: list, start: int, distances: dict, predecessor: dict, quantity: set):
    """ TODO
    """
    for node in graph:
        distances[node[0]] = float('inf')
        predecessor[node[0]] = None
        quantity.add(node[0])
    distances[start] = 0

def find_smallest_distance(nodes: set, distances: dict) -> int:
    """ TODO
    """
    target = None
    distance = float("inf")
    for node in nodes:
        if (distances[node] < distance):
            target = node
            distance = distances[node]

    return target
    
def update_distance(graph: list, u: int, v: int, distances: dict, predecessors: dict):
    """ TODO
    """
    altrernativ = distances[u] + distance_between(graph, u, v)
    if altrernativ < distances[v]:
        distances[v] = altrernativ
        predecessors[v] = u

def distance_between(graph: list, u: int, v: int) -> int:
    """ TODO
    """
    node = next((node for node in graph if (node[0] == u and node[1] == v)), None)
    if node is None:
        # TOOD: mas, what about error handling in python?
        print("Error 0001")

    return node[2]

def shortest_path(target: int, predecessors: dict) -> list:
    """ TODO
    """
    path = [target]
    u = target

    while predecessors[u] is not None:
        u = predecessors[u]
        path.insert(0, u)

    return path