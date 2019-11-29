"""To find the cosh(x) for the given value say x """

import unittest
"""This module is used to unit test the scientific operation"""
import unittest
import math
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """class for unittesting"""

    def test_for_positive_number(self):
        """test case for checking a Positive number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(1), 1.5430798443133158)

    def test_for_negative_number(self):
        """test case for checking a Positive number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(-2), 3.762190811852014)

    def test_for_positive__floating_point_number(self):
        """test case for checking a Positive floating number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(1.8), 3.1074696140087874)

    def test_for_zero(self):
        """test case for checking for Zero"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(0), 1)

    def test_for_string(self):
        """test case for checking for Zero"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh('fgftgf'), "Value error")
    """This class is used to test the scientific operations"""

    def test_tanh_integer(self):
        """test case for tanh(4)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(4), 0.9993292997390669)

    def test_tanh_zero(self):
        """test case for tanh(0)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(0), 0.0)

    def test_tanh_integer500(self):
        """test case for tanh(500)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(500), 1.0)

    def test_tanh_negative(self):
        """test case for tanh(-14)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(-14), -0.9999999999986172)

    def test_tanh_float(self):
        """test case for tanh(8.9)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(8.1), 0.9999998157280002)

    def test_tanh_fnegative(self):
        """test case for tanh(-55.7)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(-55.7), -1.0)

    def test_tanh_string(self):
        """test case for tanh(-55.7)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh("sss"), "value error(enter a number)")

    def test_10_power_x_pos_power(self):
        """This function is used to unit test the scientific operation 10 power x
         for positive power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(2), 10**2)

    def test_10_power_x_neg_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for negative power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(-2), 10**(-2))

    def test_10_power_x_zero_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for zero power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(0), 10**0)

    def test_10_power_x_pos_dec_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for positive_float power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(2.2), 10**2.2)

    def test_10_power_x_neg_dec_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for negative_float power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(-2.2), 10**(-2.2))

    def test_10_power_x_exception_power(self):
        """This function is used to unit test the scientific operation 10 power
        for negative_float power value"""
        calculate_ten_power = ScientificCalc()
        with self.assertRaises(ValueError):
            calculate_ten_power.cal_power_ten('accenture')

    def test_10_power_x_inverse(self):
        """This function is used to test for the inverse of scientific operation
        10 power x"""
        calculate_ten_power = ScientificCalc()
        value = calculate_ten_power.cal_power_ten(2)
        inverse = math.log10(value)
        self.assertEqual(inverse, 2)

    def test_e_power_x_positive_exp(self):
        "When the input is positive integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(2), 2.71828182846 ** 2)

    def test_e_power_x_negative_exp(self):
        "When the input is negative integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-2), 2.71828182846 ** -2)

    def test_e_power_x_zero_exp(self):
        "When the input is zero"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(0), 2.71828182846 ** 0)

    def test_e_power_x_pos_decimal_exp(self):
        "When the input is positive decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(8.6), 2.71828182846 ** 8.6)

    def test_e_power_x_neg_decimal_exp(self):
        "When the input is negative decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-8.6), 2.71828182846 ** -8.6)

    def test_e_power_x_try_except(self):
        "Test case for try and except"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func('accenture'),
                         "Please enter float or integer types input.")

    def test_x_power_y_posint_posint(self):
        """When both the input is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, 2), pow(2, 2))

    def test_x_power_y_negint_posint(self):
        """When power is positive integer and base is negative integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2, 2), pow(-2, 2))

    def test_x_power_y_negint_negint(self):
        """When both the input is negative integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2, -2), pow(-2, -2))

    def test_x_power_y_posint_negint(self):
        """When power is negative integer and base is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, -2), pow(2, -2))

    def test_x_power_y_posfloat_posint(self):
        """When power is negative integer and base is positive float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2.2, 2), pow(2.2, 2))

    def test_x_power_y_posfloat_negint(self):
        """When power is negative integer and base is positive float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2.2, -2), pow(2.2, -2))

    def test_x_power_y_negfloat_posint(self):
        """When power is positive integer and base is negative float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2.2, 2), pow(-2.2, 2))

    def test_x_power_y_negfloat_negint(self):
        """When power is negative integer and base is negative float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2.2, -2), pow(2.2, -2))

    def test_x_power_y_string_num(self):
        """When power is positive integer and base is string"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization("string", 2), "Value Error")

    def test_x_power_y_num_string(self):
        """When power is string and base is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, "string"), "Value Error")

