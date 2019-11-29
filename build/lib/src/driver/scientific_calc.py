"""
finding 1/x
"""
import logging

logging.basicConfig(filename="confile.log", level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')


class ScientificCalc(object):
    """init method"""
    def __init__(self):
        self.number = 0

    @classmethod
    def one_by_x(cls, number):
        """returns 1/x"""
        try:
            return float(1)/float(number)
        except ZeroDivisionError:
            logging.warning("division with zero cannot be performed")
            return "ZeroDivisionError"
        except ValueError:
            logging.warning("give an integer")
            return "ValueError"
