import unittest
from dijkstra import core

class TestDiscovery(unittest.TestCase):
    def test_discovery(self):
        hello = "Hello, World!"

        self.assertEqual(hello, "Hello, World!")

class TestDijkstra(unittest.TestCase):
    def test_general_01(self):
        node_00 = 0
        node_01 = 1
        node_02 = 2
        node_03 = 3

        dist_00_01 = 1
        dist_00_02 = 2
        dist_01_00 = 1
        dist_01_03 = 1
        dist_02_00 = 2
        dist_02_03 = 3
        dist_03_01 = 1
        dist_03_02 = 3

        connection_01 = [node_00, node_01, dist_00_01]
        connection_02 = [node_00, node_02, dist_00_02]
        connection_10 = [node_01, node_00, dist_01_00]
        connection_13 = [node_01, node_03, dist_01_03]
        connection_20 = [node_02, node_00, dist_02_00]
        connection_23 = [node_02, node_03, dist_02_03]
        connection_31 = [node_03, node_01, dist_03_01]
        connection_32 = [node_03, node_02, dist_03_02]

        graph = []
        graph.append(connection_01)
        graph.append(connection_02)
        graph.append(connection_10)
        graph.append(connection_13)
        graph.append(connection_20)
        graph.append(connection_23)
        graph.append(connection_31)
        graph.append(connection_32)

        predecessors = core.dijkstra(graph, node_00)
        shortest_path = core.shortest_path(node_03, predecessors)

        result = [node_00, node_01, node_03]

        self.assertEqual(shortest_path, result)

    def test_general_02(self):
        node_00 = 0
        node_01 = 1
        node_02 = 2
        node_03 = 3

        dist_00_01 = 3
        dist_00_02 = 2
        dist_01_00 = 3
        dist_01_03 = 1
        dist_02_00 = 2
        dist_02_03 = 1
        dist_03_01 = 1
        dist_03_02 = 1

        connection_01 = [node_00, node_01, dist_00_01]
        connection_02 = [node_00, node_02, dist_00_02]
        connection_10 = [node_01, node_00, dist_01_00]
        connection_13 = [node_01, node_03, dist_01_03]
        connection_20 = [node_02, node_00, dist_02_00]
        connection_23 = [node_02, node_03, dist_02_03]
        connection_31 = [node_03, node_01, dist_03_01]
        connection_32 = [node_03, node_02, dist_03_02]

        graph = []
        graph.append(connection_01)
        graph.append(connection_02)
        graph.append(connection_10)
        graph.append(connection_13)
        graph.append(connection_20)
        graph.append(connection_23)
        graph.append(connection_31)
        graph.append(connection_32)

        predecessors = core.dijkstra(graph, node_00)
        shortest_path = core.shortest_path(node_03, predecessors)

        result = [node_00, node_02, node_03]

        self.assertEqual(shortest_path, result)

    def test_general_03(self):
        node_00 = 0
        node_01 = 1
        node_02 = 2
        node_03 = 3
        node_04 = 4

        dist_00_01 = 3
        dist_00_02 = 2
        dist_01_00 = 3
        dist_01_03 = 1
        dist_02_00 = 2
        dist_02_03 = 1
        dist_03_01 = 1
        dist_03_02 = 1
        dist_03_04 = 1
        dist_04_03 = 1

        connection_01 = [node_00, node_01, dist_00_01]
        connection_02 = [node_00, node_02, dist_00_02]
        connection_10 = [node_01, node_00, dist_01_00]
        connection_13 = [node_01, node_03, dist_01_03]
        connection_20 = [node_02, node_00, dist_02_00]
        connection_23 = [node_02, node_03, dist_02_03]
        connection_31 = [node_03, node_01, dist_03_01]
        connection_32 = [node_03, node_02, dist_03_02]
        connection_34 = [node_03, node_04, dist_03_04]
        connection_43 = [node_04, node_03, dist_04_03]

        graph = []
        graph.append(connection_01)
        graph.append(connection_02)
        graph.append(connection_10)
        graph.append(connection_13)
        graph.append(connection_20)
        graph.append(connection_23)
        graph.append(connection_31)
        graph.append(connection_32)
        graph.append(connection_34)
        graph.append(connection_43)

        predecessors = core.dijkstra(graph, node_00)
        shortest_path = core.shortest_path(node_03, predecessors)

        result = [node_00, node_02, node_03]

        self.assertEqual(shortest_path, result)

    def test_general_04(self):
        node_00 = 0
        node_01 = 1
        node_02 = 2
        node_03 = 3
        node_04 = 4

        dist_00_01 = 3
        dist_00_02 = 2
        dist_01_00 = 3
        dist_01_03 = 1
        dist_02_00 = 2
        dist_02_03 = 1
        dist_03_01 = 1
        dist_03_02 = 1
        dist_03_04 = 1
        dist_04_03 = 1

        connection_01 = [node_00, node_01, dist_00_01]
        connection_02 = [node_00, node_02, dist_00_02]
        connection_10 = [node_01, node_00, dist_01_00]
        connection_13 = [node_01, node_03, dist_01_03]
        connection_20 = [node_02, node_00, dist_02_00]
        connection_23 = [node_02, node_03, dist_02_03]
        connection_31 = [node_03, node_01, dist_03_01]
        connection_32 = [node_03, node_02, dist_03_02]
        connection_34 = [node_03, node_04, dist_03_04]
        connection_43 = [node_04, node_03, dist_04_03]

        graph = []
        graph.append(connection_01)
        graph.append(connection_02)
        graph.append(connection_10)
        graph.append(connection_13)
        graph.append(connection_20)
        graph.append(connection_23)
        graph.append(connection_31)
        graph.append(connection_32)
        graph.append(connection_34)
        graph.append(connection_43)

        predecessors = core.dijkstra(graph, node_00)
        shortest_path = core.shortest_path(node_04, predecessors)

        result = [node_00, node_02, node_03, node_04]

        self.assertEqual(shortest_path, result)

    def test_general_05(self):
        node_00 = 0
        node_01 = 1
        node_02 = 2
        node_03 = 3
        node_04 = 4

        dist_00_01 = 3
        dist_00_02 = 2
        dist_01_00 = 3
        dist_01_03 = 1
        dist_02_00 = 2
        dist_02_03 = 1
        dist_03_01 = 1
        dist_03_02 = 1
        dist_03_04 = 1
        dist_04_03 = 1

        connection_01 = [node_00, node_01, dist_00_01]
        connection_02 = [node_00, node_02, dist_00_02]
        connection_10 = [node_01, node_00, dist_01_00]
        connection_13 = [node_01, node_03, dist_01_03]
        connection_20 = [node_02, node_00, dist_02_00]
        connection_23 = [node_02, node_03, dist_02_03]
        connection_31 = [node_03, node_01, dist_03_01]
        connection_32 = [node_03, node_02, dist_03_02]
        connection_34 = [node_03, node_04, dist_03_04]
        connection_43 = [node_04, node_03, dist_04_03]

        graph = []
        graph.append(connection_01)
        graph.append(connection_02)
        graph.append(connection_10)
        graph.append(connection_13)
        graph.append(connection_20)
        graph.append(connection_23)
        graph.append(connection_31)
        graph.append(connection_32)
        graph.append(connection_34)
        graph.append(connection_43)

        predecessors = core.dijkstra(graph, node_01)
        shortest_path = core.shortest_path(node_04, predecessors)

        result = [node_01, node_03, node_04]

        self.assertEqual(shortest_path, result)

    def test_general_06(self):
        node_00 = 0
        node_01 = 1
        node_02 = 2
        node_03 = 3
        node_04 = 4

        dist_00_01 = 3
        dist_00_02 = 2
        dist_01_00 = 3
        dist_01_03 = 1
        dist_02_00 = 2
        dist_02_03 = 1
        dist_03_01 = 1
        dist_03_02 = 1
        dist_03_04 = 1
        dist_04_03 = 1

        connection_01 = [node_00, node_01, dist_00_01]
        connection_02 = [node_00, node_02, dist_00_02]
        connection_10 = [node_01, node_00, dist_01_00]
        connection_13 = [node_01, node_03, dist_01_03]
        connection_20 = [node_02, node_00, dist_02_00]
        connection_23 = [node_02, node_03, dist_02_03]
        connection_31 = [node_03, node_01, dist_03_01]
        connection_32 = [node_03, node_02, dist_03_02]
        connection_34 = [node_03, node_04, dist_03_04]
        connection_43 = [node_04, node_03, dist_04_03]

        graph = []
        graph.append(connection_01)
        graph.append(connection_02)
        graph.append(connection_10)
        graph.append(connection_13)
        graph.append(connection_20)
        graph.append(connection_23)
        graph.append(connection_31)
        graph.append(connection_32)
        graph.append(connection_34)
        graph.append(connection_43)

        predecessors = core.dijkstra(graph, node_04)
        shortest_path = core.shortest_path(node_00, predecessors)

        result = [node_04, node_03, node_02, node_00]

        self.assertEqual(shortest_path, result)

if __name__ == '__main__':
    unittest.main()
