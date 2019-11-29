import unittest
from src.driver.ScientificCalc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):
    """test Class for the factorial of a number"""
    # test_for_valid_number

    def test_valid_number1(self):
        """test the valid number"""
        result = ScientificCalc()
        self.assertEqual(result.factorial_number(4), 24)
    # test_for_number_0

    def test_valid_number2(self):
        """test the valid number 0"""
        result = ScientificCalc()

        self.assertEqual(result.factorial_number(0), 1)
    # test_for_number_1

    def test_valid_number3(self):
        """test the valid number 1"""
        result = ScientificCalc()
        self.assertEqual(result.factorial_number(1), 1)
    # test_for_negative

    def test_negative_number(self):
        """test the negative number"""

        self.assertRaises(ValueError)

    # test_for_float
    def test_float_number(self):
        """test the float number"""
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()