"""This module is to execute scientific calculator functions"""
import math
import logging

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')

class ScientificCalc:
    """This class is used to calculate the scientific operations"""

    @classmethod
    def sin_func(cls, angle):
        """This function is used to calculate the sin function"""
        try:
            cls.value = math.sin(float(angle))
            return cls.value
        except ValueError as error:
            logging.exception(error)
            print(error)
            return "Please enter float or integer types input."
