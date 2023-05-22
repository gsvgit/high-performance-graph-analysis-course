import itertools

import networkx as nx
import queue
import boltons.queueutils


def dijkstra(src: int, graph: nx.DiGraph):
    dists = {node: float("inf") for node in graph.nodes}
    dists[src] = 0

    q = queue.PriorityQueue()
    q.put((0, src))

    while not q.empty():
        d, v = q.get()

        if d > dists[v]:
            continue

        for u in graph.neighbors(v):
            new_dist = dists[v] + 1

            if new_dist < dists[u]:
                dists[u] = new_dist
                q.put((new_dist, u))

    return dists


class DynSssp:
    def __init__(self, src: int, graph: nx.DiGraph):
        self.graph = graph
        self.src = src
        self.dists = dijkstra(src, graph)
        self.updated_nodes = set()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)
        self.updated_nodes.add(v)

        if u not in self.dists:
            self.dists[u] = float("inf")

        if v not in self.dists:
            self.dists[v] = float("inf")

    def remove_edge(self, u, v):
        self.graph.remove_edge(u, v)
        self.updated_nodes.add(v)

    def update_dists(self):
        q = boltons.queueutils.PriorityQueue(priority_key=lambda p: p)
        curr_dists = {}

        for v in self.updated_nodes:
            curr_dists[v] = self.rhs(v)

            if curr_dists[v] != self.dists[v]:
                q.add(v, min(curr_dists[v], self.dists[v]))

        while len(q) > 0:
            v = q.pop()
            inconsistent_nodes = self.graph.successors(v)

            if curr_dists[v] < self.dists[v]:
                self.dists[v] = curr_dists[v]
            elif self.dists[v] < curr_dists[v]:
                self.dists[v] = float("inf")
                inconsistent_nodes = itertools.chain(inconsistent_nodes, [v])

            for u in inconsistent_nodes:
                curr_dists[u] = self.rhs(u)
                if curr_dists[u] != self.dists[u]:
                    q.add(u, min(curr_dists[u], self.dists[u]))
                else:
                    if v in q._entry_map:
                        q.remove(v)

    def get_dists(self):
        if len(self.updated_nodes) > 0:
            self.update_dists()
            self.updated_nodes.clear()

        return self.dists

    def rhs(self, v):
        if v == self.src:
            return 0

        return min(
            (self.dists[u] + 1 for u in self.graph.predecessors(v)),
            default=float("inf"),
        )
