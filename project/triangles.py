from pygraphblas import Matrix, UINT64, BOOL, descriptor
from typing import List


def each_vertex_triangles(graph: Matrix) -> List[int]:
    """
    For each vertex in Graph, counts the number of triangles in which they consist

    :param graph: Boolean adjacency matrix of Graph
    :return: list where i-th element is triangles number for i-th vertex
    """
    assert graph.type == BOOL
    assert graph.square

    graph.assign_scalar(False, mask=Matrix.identity(BOOL, graph.nrows) & graph)

    triangles = graph.mxm(graph, UINT64.PLUS_TIMES, mask=graph).reduce_vector()
    triangles.assign_scalar(0, mask=triangles, desc=descriptor.C)

    return [i // 2 for i in triangles.vals]


def cohen_triangles(graph: Matrix) -> int:
    """
    Count triangles number in graph by Cohen's algorithm

    :param graph: Boolean adjacency matrix of Graph
    :return: Triangles number
    """
    assert graph.type == BOOL
    assert graph.square

    lower_matrix = graph.tril(-1)
    upper_matrix = graph.triu(1)

    triangles = (
        lower_matrix.mxm(
            upper_matrix,
            UINT64.PLUS_TIMES,
            mask=lower_matrix | upper_matrix,
        ).reduce_int()
        // 2
    )

    return triangles


def sandia_triangles(graph: Matrix) -> int:
    """
    Count triangles number in graph by Sandia's algorithm

    :param graph: Boolean adjacency matrix of Graph
    :return: Triangles number
    """
    assert graph.type == BOOL
    assert graph.square

    lower_matrix = graph.tril(-1)

    triangles = lower_matrix.mxm(
        lower_matrix.transpose(),
        UINT64.PLUS_TIMES,
        mask=lower_matrix,
    ).reduce_int()

    return triangles
