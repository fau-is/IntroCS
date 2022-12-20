import unittest
from graph_drawer import draw_graph_from_mat

class TestDetectsUnsymmetricMatrix(unittest.TestCase):
    def setUp(self):
        self.matrices =
        [
            [
                [0, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 1, 0],
            ],
            [
                [0, 1, 2, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
            ]

        ]

    def test_non_symmetric():



    def test_with_weights():