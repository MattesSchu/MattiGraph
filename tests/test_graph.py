import unittest
from dijkstra import graph

class TestGraph(unittest.TestCase):
    
    def test_init(self):
        g_raph = graph.Graph()
        n_ode = graph.Node()