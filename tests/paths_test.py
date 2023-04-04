import project.shortest_paths as sp
from pygraphblas import Matrix
from math import inf

# test_data_ms_bfs = (
#     Matrix.from_lists([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], True),
#     [
#         ([1], [(1, [-2, -1, 1, 2, 3, 4])]),
#         ([1, 2], [(1, [-2, -1, 1, 2, 3, 4]), (2, [-2, -2, -1, 2, 3, 4])]),
#         (
#             [0, 1, 2, 3, 4],
#             [
#                 (0, [-1, 0, 1, 2, 3, 4]),
#                 (1, [-2, -1, 1, 2, 3, 4]),
#                 (2, [-2, -2, -1, 2, 3, 4]),
#                 (3, [-2, -2, -2, -1, 3, 4]),
#                 (4, [-2, -2, -2, -2, -1, 4]),
#             ],
#         ),
#     ],
# )

test_data_sssp = {
    "graph": Matrix.from_lists(
        [0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
    ),
    "sources": [0, 1, 2, 3, 4, 5],
    "ans": [
        [0.0, 1.0, 3.0, 6.0, 9.0, 11.0],
        [inf, 0.0, 2.0, 5.0, 8.0, 10.0],
        [inf, inf, 0.0, 3.0, 6.0, 8.0],
        [inf, inf, inf, 0.0, 3.0, 5.0],
        [inf, inf, inf, inf, 0.0, 2.0],
        [inf, inf, inf, inf, inf, 0.0],
    ],
}

test_data_mssp = {
    "graph": Matrix.from_lists(
        [0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
    ),
    "sources": [[0, 1], [2, 3], [0, 5]],
    "ans": [
        [(0, [0.0, 1.0, 3.0, 6.0, 9.0, 11.0]), (1, [inf, 0.0, 2.0, 5.0, 8.0, 10.0])],
        [(2, [inf, inf, 0.0, 3.0, 6.0, 8.0]), (3, [inf, inf, inf, 0.0, 3.0, 5.0])],
        [(0, [0.0, 1.0, 3.0, 6.0, 9.0, 11.0]), (5, [inf, inf, inf, inf, inf, 0.0])],
    ],
}

test_data_apsp = {
    "graph": Matrix.from_lists(
        [0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
    ),
    "ans": [
        (0, [0.0, 1.0, 3.0, 6.0, 9.0, 11.0]),
        (1, [inf, 0.0, 2.0, 5.0, 8.0, 10.0]),
        (2, [inf, inf, 0.0, 3.0, 6.0, 8.0]),
        (3, [inf, inf, inf, 0.0, 3.0, 5.0]),
        (4, [inf, inf, inf, inf, 0.0, 2.0]),
        (5, [inf, inf, inf, inf, inf, 0.0]),
    ],
}


def test_sssp():
    for i, s in enumerate(test_data_sssp["sources"]):
        assert sp.sssp(test_data_sssp["graph"], s) == test_data_sssp["ans"][i]


def test_mssp():
    for i, s in enumerate(test_data_mssp["sources"]):
        assert sp.mssp(test_data_mssp["graph"], s) == test_data_mssp["ans"][i]


def test_apsp():
    assert sp.apsp(test_data_apsp["graph"]) == test_data_apsp["ans"]
