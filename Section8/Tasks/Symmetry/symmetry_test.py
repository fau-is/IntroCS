import unittest
from symmetry import is_matrix_symmetric

class TestDetectsUnsymmetricMatrix(unittest.TestCase):
    def setUp(self):
        self.matrices = [
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

    def test_non_symmetric(self):
        self.assertFalse(is_matrix_symmetric(self.matrices[0]))

    def test_with_weights(self):
        self.assertFalse(is_matrix_symmetric(self.matrices[1]))

class TestDetectsSymmetricMatrix(unittest.TestCase):
    def setUp(self):
        self.matrices = [
            [
                [0, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
            ],
            [
                [0, 1, 2, 3],
                [1, 0, 0, 0],
                [2, 0, 0, 0],
                [3, 0, 0, 0],
            ]

        ]

    def test_symmetric(self):
        self.assertTrue(is_matrix_symmetric(self.matrices[0]))

    def test_with_weights(self):
        self.assertTrue(is_matrix_symmetric(self.matrices[1]))

if __name__ == '__main__':
    unittest.main()