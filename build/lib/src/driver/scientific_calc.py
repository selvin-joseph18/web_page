<<<<<<< HEAD
"""The function is defined here"""

import logging


class ScientificCalc:
    """This is the class of main logic program """
    def __init__(self):
        self.number = 0
        self.result = 0

    @classmethod
    def trig_cosh(cls, number):
        """The function to calculate cosh"""
        logging.basicConfig(filename="ScientificCalculatorLog.log", level=logging.DEBUG,
                            format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')
        try:
            if "." in str(number):
                number = float(number)
            else:
                number = int(number)
            calculate = 2.71828 ** number / 2 + 2.71828 ** -number / 2
            return calculate
        except ValueError as e_value:
            logging.exception(e_value)
            return "Value error"
=======
"""This module is to execute scientific calculator functions"""
import math
import logging

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')

class ScientificCalc:
    """This class is used to calculate the scientific operations"""

    def __init__(self):
        self.power = 0
        self.result = 0
        self.base = 0
        self.angle = 0
        self.tanhx = 0

    @classmethod
    def cal_power_ten(cls, pow_value):
        """This function is used to calculate ten power x value"""
        try:
            cls.answer = 10**float(pow_value)
            return cls.answer
        except ValueError as value_error:
            logging.error(value_error)
            raise ValueError

    @classmethod
    def exponential_func(cls, power_value):
        """This function is used to calculate the exponential function"""
        try:
            cls.power = float(power_value)
            exp_value = 2.71828182846
            cls.result = exp_value ** cls.power
            return cls.result
        except ValueError as error:
            logging.exception(error)
            print(error)
            return "Please enter float or integer types input."

    @classmethod
    def x_power_y(cls, base_val, power_val):
        """if power value is 0 returns 1
        else recursively calls x_power_y function and returns the final answer"""
        cls.answer = 1
        if power_val == 0:
            return 1
        elif power_val % 2 == 0:
            return (cls.x_power_y(base_val, int(power_val / 2)) *
                    cls.x_power_y(base_val, int(power_val / 2)))
        else:
            if power_val > 0:
                return (base_val * cls.x_power_y(base_val, int(power_val / 2)) *
                        cls.x_power_y(base_val, int(power_val / 2)))
            else:
                return (cls.x_power_y(base_val, int(power_val / 2)) *
                        cls.x_power_y(base_val, int(power_val / 2))) / base_val

    @classmethod
    def var_initialization(cls, base_no, power_no):
        """initializing the variables"""
        try:
            base = float(base_no)
            power = int(power_no)
            return cls.x_power_y(base, power)
        except ValueError as error:
            logging.exception(error)
            return "Value Error"

    @classmethod
    def calculate_tanh(cls, angle):
        """A method to calculate tanh"""
        try:
            cls.angle = angle
            cls.angle = float(cls.angle)
            exponential = math.e
            coshx = ((exponential ** cls.angle) + (exponential ** -cls.angle))
            sinhx = ((exponential ** cls.angle) - (exponential ** -cls.angle))
            cls.tanhx = sinhx / coshx
            return cls.tanhx
        except ValueError as error:
            logging.exception(error)
            return "value error(enter a number)"
>>>>>>> b405f71bbc91cc713782c97c443adea95cbeff2e
