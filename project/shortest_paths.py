from pygraphblas import Matrix, FP64
import math

from typing import List, Tuple


def sssp(graph: Matrix, source: int) -> List[int]:
    """
    Search the shortest paths for single source
    :param graph: float adjacency matrix of graph
    :param source: source vertex
    :return: list where i-th element is distance from source to vertex i
    """
    return mssp(graph, [source])[0][1]


def mssp(graph: Matrix, sources: List[int]) -> List[Tuple[int, List[int]]]:
    """
    Search the shortest paths for multiple sources
    :param graph: float adjacency matrix of graph
    :param sources: list of source vertices
    :return: list where i-th element is the pair (source, distances) for i-th vertex
    """

    assert graph.type == FP64
    assert graph.square
    for source in sources:
        assert source in range(graph.nrows)

    graph = _zeros_on_main_diag(graph)

    dists = Matrix.sparse(FP64, nrows=len(sources), ncols=graph.nrows)
    for i, source in enumerate(sources):
        dists[i, source] = 0

    for _ in range(graph.nrows - 1):
        dists = dists.mxm(graph, FP64.MIN_PLUS)

    if dists.isne(dists.mxm(graph, FP64.MIN_PLUS)):
        raise ValueError("Negative cycle detected")

    return [
        (source, [dists.get(i, j, default=math.inf) for j in range(graph.nrows)])
        for i, source in enumerate(sources)
    ]


def apsp(graph: Matrix) -> List[Tuple[int, List[int]]]:
    """
    Search the shortest paths for all pair of vertices
    :param graph: float adjacency matrix of graph
    :return: list where i-th element is pair (source, dist) for i-th vertex
    """

    assert graph.type == FP64
    assert graph.square

    graph = _zeros_on_main_diag(graph)
    dists = graph

    for i in range(graph.nrows):
        col, row = dists.extract_matrix(col_index=i), dists.extract_matrix(row_index=i)
        dists.eadd(
            col.mxm(row, FP64.MIN_PLUS),
            FP64.MIN,
            out=dists,
        )

    for k in range(graph.nrows):
        col, row = dists.extract_matrix(col_index=k), dists.extract_matrix(row_index=k)
        if dists.isne(
            dists.eadd(
                col.mxm(row, FP64.MIN_PLUS),
                FP64.MIN,
            )
        ):
            raise ValueError("Negative cycle detected")

    return [
        (i, [dists.get(i, j, default=math.inf) for j in range(graph.nrows)])
        for i in range(graph.nrows)
    ]


def _zeros_on_main_diag(matrix: Matrix) -> Matrix:
    copy = matrix.dup()
    for i in range(matrix.ncols):
        copy[i, i] = 0.0
    return copy
