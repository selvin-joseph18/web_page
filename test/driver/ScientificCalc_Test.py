
"""test cases for 1/x"""
import unittest
from src.driver.ScientificCalc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):
    """test case"""

    def test_one_by_x_value(self):
        """input=1"""
        calc = ScientificCalc()
        res = calc.one_by_x(1)
        self.assertEqual(res, 1)

    def test_one_by_x_zero_division_error(self):
        """input=0"""
        calc = ScientificCalc()
        self.assertEqual(calc.one_by_x(0), "ZeroDivisionError")

    def test_one_by_x_value_error(self):
        """input=giving string instead of number"""
        calc = ScientificCalc()
        result = calc.one_by_x("s")
        self.assertEqual(result, "ValueError")

    def test_one_by_x_value5(self):
        """when we take 5 as input"""
        calc = ScientificCalc()
        result = calc.one_by_x(5)
        self.assertEqual(result, 0.2)


if __name__ == "__main__":
    unittest.main()
