from project.dyn_sp import dijkstra, DynSssp
import networkx as nx

test_graph = nx.DiGraph()
test_graph.add_edge(0, 1)
test_graph.add_edge(1, 2)
test_graph.add_edge(2, 3)
test_graph.add_edge(3, 4)


def test_dijkstra():
    assert dijkstra(0, test_graph) == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}


def test_dyn_sssp():
    algo = DynSssp(0, test_graph)
    assert algo.get_dists() == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    algo.add_edge(0, 2)
    algo.remove_edge(0, 1)
    assert algo.get_dists() == {0: 0, 1: float("inf"), 2: 1, 3: 2, 4: 3}
