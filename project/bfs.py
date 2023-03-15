from pygraphblas import Matrix, BOOL, Vector, INT64
from typing import List


def bfs(graph: Matrix, source: int) -> List[int]:

    assert graph.type == BOOL
    assert graph.square
    assert source in range(graph.nrows)

    n = graph.nrows

    front = Vector.sparse(BOOL, n)
    visited = Vector.sparse(BOOL, n)
    result = Vector.dense(INT64, n, fill=-1)

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
