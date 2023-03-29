from pygraphblas import Matrix, BOOL, Vector, INT64, descriptor
from typing import List, Tuple


def bfs(graph: Matrix, source: int) -> List[int]:
    """
    BFS for directed graph with source vertex

    :param graph: boolean adjacency matrix of graph
    :param source: source vertex
    :return: list where i-th element is distance to i-th graph vertex
    """
    assert graph.type == BOOL
    assert graph.square
    assert source in range(graph.nrows)

    n = graph.nrows

    front = Vector.sparse(BOOL, n)
    visited = Vector.sparse(BOOL, n)
    result = Vector.dense(INT64, n, -1)

    front[source] = True
    current = 0
    prev = None

    while prev != visited.nvals:
        prev = visited.nvals
        result.assign_scalar(current, mask=front)
        visited |= front
        front = front.vxm(graph)
        front.assign_scalar(False, mask=visited)
        current += 1

    return list(result.vals)


def ms_bfs(graph: Matrix, sources: List[int]) -> List[Tuple[int, List[int]]]:
    """
    Multi-source BFS for directed graph with source vertices

    :param graph: boolean adjacency matrix of graph
    :param sources: list of source vertices
    :return: list of pairs where first - source vertex, second - list of parents
    """
    assert graph.type == BOOL
    assert graph.square
    for source in sources:
        assert source in range(graph.nrows)

    parents = Matrix.sparse(INT64, len(sources), graph.ncols)
    front = Matrix.sparse(INT64, len(sources), graph.ncols)

    for i, v in enumerate(sources):
        parents[i, v] = -1
        front[i, v] = v

    while front:
        front.mxm(
            graph, INT64.MIN_FIRST, None, front, parents.pattern(), None, descriptor.RC
        )
        parents.assign(front, None, None, front.pattern())
        front.apply(INT64.POSITIONJ, front, front.pattern())

    return [
        (source, [parents.get(i, col, -2) for col in range(graph.ncols)])
        for i, source in enumerate(sources)
    ]
