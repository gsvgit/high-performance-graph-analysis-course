import pytest
from pygraphblas import Matrix
from project.bfs import bfs

test_data = (
    Matrix.from_lists(
        [0, 1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 5],
        True
    ),
    [
        (0, [0, 1, 2, 3, 4, 5]),
        (1, [-1, 0, 1, 2, 3, 4]),
        (2, [-1, -1, 0, 1, 2, 3]),
        (3, [-1, -1, -1, 0, 1, 2]),
        (4, [-1, -1, -1, -1, 0, 1]),
        (5, [-1, -1, -1, -1, -1, 0])
    ]
)


def test_bfs_works_correctly():
    for source, ans in test_data[1]:
        assert bfs(test_data[0], source) == ans
