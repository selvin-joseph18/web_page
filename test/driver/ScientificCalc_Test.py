"""unit test case for square root"""

import unittest
from src.driver.ScientificCalc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):
    """ test cases"""
    def test_square_root_positive(self):
        """test case for positive value"""
        test=ScientificCalc()
        self.assertEqual(test.square_root(4), 2.0)

    def test_square_root_negative(self):
        """test case for negative value"""
        test =ScientificCalc()
        self.assertEqual(test.square_root(-8), complex(1.7319121124709868e-16 + 2.8284271247461903j))

    def test_square_root_string(self):
        """test case if we give string"""
        test = ScientificCalc()
        self.assertEqual(test.square_root("a"), "expecting integer value")


if __name__ == '__main__':
    unittest.main()
