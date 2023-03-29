from pygraphblas import Matrix
from project import triangles as t

test_data = [
    (
        Matrix.from_lists([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], True),
        {"each_vertex": [0, 0, 0, 0, 0, 0], "cohen": 0, "sandia": 0},
    ),
    (
        Matrix.from_lists(
            [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 2, 3, 0, 2, 3, 0, 1, 3, 0, 1, 2],
            True,
        ),
        {"each_vertex": [3, 3, 3, 3], "cohen": 4, "sandia": 4},
    ),
]


def test_each_vertex_triangle():
    for data, answer in test_data:
        assert t.each_vertex_triangles(data) == answer["each_vertex"]


def test_cohen_triangle():
    for data, answer in test_data:
        assert t.cohen_triangles(data) == answer["cohen"]


def test_sandia_triangle():
    for data, answer in test_data:
        assert t.sandia_triangles(data) == answer["sandia"]
