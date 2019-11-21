"""This module is used for calculating scientific operation(e^x)"""
import logging


logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')


class ScientificCalc:
    """This class contains exponential_func method"""
    def __init__(self):
        self.power = 0
        self.result = 0

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
