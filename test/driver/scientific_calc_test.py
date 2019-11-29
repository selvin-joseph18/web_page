"""importing module"""
import unittest
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """main class of the program"""
    def test_addition(self):
        """calculating the positive addition value"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition(2, 2), 4)

    def test_subtraction(self):
        """calculating the subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction(5, 3), 2)

    def test_multipy(self):
        """calculating the multiplication """
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication(5, 3), 15)

    def test_divide(self):
        """calculating the division"""
        calc = ScientificCalc()
        self.assertEqual(calc.division(4, 2), 2)

    def test_error(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition(2, 'a'), "Enter only numbers")

    def test_zeroerror(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.division(2, 0), "Enter a number greater than zero")


if __name__ == '__main__':
    unittest.main()
