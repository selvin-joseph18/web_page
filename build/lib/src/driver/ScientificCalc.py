"""math_module"""
import math
import logging

logging.basicConfig(filename="new_log.log", level=logging.INFO,
                    format='%(name)s - %(levelname)s - %(message)s',
                    filemode='w')

"""function_logarithm"""


class ScientificCalc:
    def __init__(self,number=0):
        self.number = number
    @classmethod
    def logarithm(self, number):
        """check for log base 10 of a number"""
        try:
            if number > 0:
                k = math.log10(number)
                return k
            elif type(number) != int:
                raise TypeError
            else:
                raise ValueError
        except ValueError as value_error:
            logging.error(value_error.message)
            print "enter positive values"
            return 'ValueError'
        except TypeError as type_error:
            logging.error(type_error.message)
            print "enter integer or float"
            return 'TypeError'


