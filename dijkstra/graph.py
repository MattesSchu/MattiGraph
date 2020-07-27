
class Node():
    """TODO
        - add a object identifier
        - add connections
    """

    def __init__(self):
        """TODO
        """
        self.name = ""

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
            hash(self) == hash(other))

class Connection():
    """TODO
        - weighted connection between 2 nodes
    """
    
    def __init__(self, first: Node, second: Node, weight: int):
        self.first = first
        self.second = second
        self.weight = weight

    def __str__(self) -> str:
        return "From " + self.first + " to " + self.second + " with distance " + self.weight

    def __hash__(self) -> int:
        return hash(hash(self.first) + hash(self.second) + self.weight)

    def __eq__(self, other: Connection) -> bool:
        return (self.__class__ == other.__class__ and
            hash(self) == hash(other))
            

class Graph():
    """ TODO
    """
    
    def __init__(self):
        """TODO
        """
        self.nodes = list()
        self.connections = list()

    def insert_node(self, idx: int, node: Node) -> bool:
        """ TODO

            return: false if node was alrdy present.
        """ 
        if idx < 0 or idx > len(self.nodes):
            return False

        if node is None or node.name is None or node in self.nodes:
            return False

        self.nodes.insert(idx, node)
        return True

    def add_connection(self, connection) -> bool:
        """TODO
        """
        if connection in self.connections:
            print("Cannot add already existing connection.")
            return False
        
        self.connections.append(connection)
        return True


    def connect_nodes(self, first: Node, second: Node, weight) -> bool:
        """TODO
        """
        if first is None or second is None:
            print("Nodes cannot be None.")
            return False
        if first.name is None or second.name is None:
            print("The nodes must have names.")
            return False
        if weight < 0:
            print("Weight cannot be negative.")
            return False
        if first not in self.nodes or second not in self.nodes:
            print("Nodes to connect are not in the graph.")
            return False

        connection = Connection(first, second, weight)
        return self.add_connection(connection)


    def append_node(self, node: Node):
        """TODO
        """
        if node.name is None or node in self.nodes:
            return False
        self.nodes.append(node)
        return True

    def remove_node(self, node: Node) -> bool:
        """TODO
        """
        if node is None or node not in self.nodes:
            return False

        self.nodes.remove(node)

    def remove_node_at_idx(self, idx: int):
        """TODO
        """
        self.nodes.remove(idx)

    def __str__(self):
        """TODO
        """



    