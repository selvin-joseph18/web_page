"""importing a unittest case"""
import unittest
from src.driver.ScientificCalc import scientific_calc


class TestCubeRoot(unittest.TestCase):
    """test case"""

    def test_cube_root(self):
        """test case for check cube root"""
        test = scientific_calc()
        self.assertEqual(test.cube_root(8), 2)

    def test_cube_root_negative(self):
        """test case for check cube root"""
        test = scientific_calc()
        self.assertEqual(test.cube_root(-8), -2)

    def test_cube_root1(self):
        """test case for exception"""
        test = scientific_calc()
        self.assertEqual(test.cube_root("hai"), "ValueError")


if __name__ == '__main__':
    unittest.main()
