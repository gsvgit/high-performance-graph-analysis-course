import pytest
from pygraphblas import Matrix
from project.bfs import bfs, ms_bfs

test_data_bfs = (
    Matrix.from_lists([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], True),
    [
        (0, [0, 1, 2, 3, 4, 5]),
        (1, [-1, 0, 1, 2, 3, 4]),
        (2, [-1, -1, 0, 1, 2, 3]),
        (3, [-1, -1, -1, 0, 1, 2]),
        (4, [-1, -1, -1, -1, 0, 1]),
        (5, [-1, -1, -1, -1, -1, 0]),
    ],
)

test_data_ms_bfs = (
    Matrix.from_lists([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], True),
    [
        ([1], [(1, [-2, -1, 1, 2, 3, 4])]),
        ([1, 2], [(1, [-2, -1, 1, 2, 3, 4]), (2, [-2, -2, -1, 2, 3, 4])]),
        (
            [0, 1, 2, 3, 4],
            [
                (0, [-1, 0, 1, 2, 3, 4]),
                (1, [-2, -1, 1, 2, 3, 4]),
                (2, [-2, -2, -1, 2, 3, 4]),
                (3, [-2, -2, -2, -1, 3, 4]),
                (4, [-2, -2, -2, -2, -1, 4]),
            ],
        ),
    ],
)


def test_bfs_works_correctly():
    for source, ans in test_data_bfs[1]:
        assert bfs(test_data_bfs[0], source) == ans


def test_works_as_expected():
    for sources, ans in test_data_ms_bfs[1]:
        assert ms_bfs(test_data_ms_bfs[0], sources) == ans
