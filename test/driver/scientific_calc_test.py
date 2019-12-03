"""importing module"""
import unittest
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """main class of the program"""
    def test_add_two_positive(self):
        """calculating the two positive addition value"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2]), 4)

    def test_add_one_negative(self):
        """calculating the one addition and one subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([-2, 4]), 2)

    def test_one_negetive(self):
        """calculating with alternate sign """
        calc = ScientificCalc()
        self.assertEqual(calc.addition([4, -2]), 2)

    def test_add_two_negative(self):
        """calculating two addition value with negative"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([-2, -2]), -4)

    def test_add_multiple_positive(self):
        """calculating the multiple positive addition value"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2, 3, 4, 5]), 16)

    def test_addition(self):
        """calculating the multiple positive addition value with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2, -3, 4, 5]), 10)

    def test_add_alternate_negative(self):
        """calculating the alternate sign positive addition"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, -2, -3, 4, 5]), 6)

    def test_add_floatvalue(self):
        """calculating the float positive addition"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2.5]), 4.5)

    def test_add_negative_floatvalue(self):
        """calculating the addition value with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([-2.5, 3.5]), 1)

    def test_error_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 'a']), "Enter only numbers")

    def test_sub_two_positive(self):
        """calculating the subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([4, 2]), 2)

    def test_sub_one_negative(self):
        """calculating the subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-2, 4]), -6)

    def test_one_sub_negetive(self):
        """calculating the subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([4, -2]), 6)

    def test_sub_two_negative(self):
        """calculating the two negative subtraction  value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-7, -2]), -5)

    def test_sub_multiple_positive(self):
        """calculating the multiple subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, 2, 3, 4, 5]), -12)

    def test_sub_alternate_negative(self):
        """calculating the multiple subtraction with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, -2, -3, 4, 5]), -2)

    def test_sub_floatvalue(self):
        """calculating the float subtraction  value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, 2.5]), -0.5)

    def test_sub_negative_floatvalue(self):
        """calculating the negative float subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-2.5, 3.5]), -6)

    def test_sub_negative_multiple_floatvalue(self):
        """calculating the multiple float subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-2.5, 3.5, 4.5, 8, -2.7]), -15.8)

    def test_error_sub_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, 'a']), "Enter only numbers")

    def test_mul_two_positive(self):
        """calculating the positive multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([4, 2]), 8)

    def test_mul_one_negative(self):
        """calculating the negative multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-2, 4]), -8)

    def test_mul_two_negative(self):
        """calculating the two negative multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-7, -2]), 14)

    def test_mul_five_positive(self):
        """calculating the multiple multiplication  value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 2, 3, 4, 5]), 240)

    def test_mul(self):
        """calculating the multiplication value with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 2, -3, 4, 5]), -240)

    def test_mul_floatvalue(self):
        """calculating the float multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 2.5]), 5)

    def test_mul_negative_floatvalue(self):
        """calculating the negative float multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-2.5, 3.5]), -8.75)

    def test_mul_negative_multiple_floatvalue(self):
        """calculating the multiple negative float multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-2.5, 3.5, 4.5, 8, -2.7]), 850.5)

    def test_error_mul_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 'a']), "Enter only numbers")

    def test_div_two_positive(self):
        """calculating the positie division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([4, 2]), 2)

    def test_div_one_negative(self):
        """calculating the negative sign division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-2, 4]), -0.5)

    def test_div_two_negative(self):
        """calculating the two negative sign division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-7, -2]), 3.5)

    def test_div_multiple_positive(self):
        """calculating the multiple division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 2, 3, 4, 5]), 0.016666666666666666)

    def test_div_negative(self):
        """calculating the negative sign multiple division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 2, -3]), -0.3333333333333333)

    def test_div_floatvalue(self):
        """calculating the float division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 2.5]), 0.8)

    def test_div_negative_floatvalue(self):
        """calculating the negative float division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-2.5, 3.5]), -0.7142857142857143)

    def test_div_negative_multiple_floatvalue(self):
        """calculating the multiple float division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-2.5, 3.5, 4.5, 8, -2.7]), 0.00734861845972957)

    def test_error_div_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 'a']), "Enter only numbers")

    def test_zeroerror(self):
        """zero division error"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 0]), "Enter a number greater than zero")


if __name__ == '__main__':
    unittest.main()
