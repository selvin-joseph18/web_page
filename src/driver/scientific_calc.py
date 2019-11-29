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
