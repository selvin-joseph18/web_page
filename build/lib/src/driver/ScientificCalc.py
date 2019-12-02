<<<<<<< HEAD
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

=======
"""Program for calculating square root"""
import logging
logging.basicConfig(filename="confile.log", level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')


class ScientificCalc:
    def __init__(self,x_value):
        self.x_value=x_value

    @classmethod
    def square_root(self,x_value):
        """function for calculating square root"""
        try:
            x_value = int(x_value)
            if x_value >= 0:
                return x_value**0.5
            elif x_value < 0:
                imaginary_no = complex(x_value)**0.5
                return imaginary_no
        except ValueError:
            logging.error(ValueError.message)
            return "expecting integer value"
>>>>>>> b0886e731bbe124f7f8e6c655e3d02a0e8383af0

