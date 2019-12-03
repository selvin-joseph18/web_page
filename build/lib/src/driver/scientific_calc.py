"""Performing Arithmetic Operation"""

import logging
logging.basicConfig(filename="ScientificCalculatorLog.log", level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='w')


class ScientificCalc:
    """class Scientific"""

    def __init__(self):
        """constructor"""

        self.a_input = 0
        self.b_input = 0

    @classmethod
    def addition(cls, list_add):
        """calculating addition function"""
        sum = 0
        try:
            for i in list_add:
                sum = sum + float(i)
            return sum

        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"

    @classmethod
    def subtraction(cls, list_sub):
        """calculating subtraction function"""
        try:
            sub = float(list_sub[0])
            for i in range(1,len(list_sub)):
                sub = sub - float(list_sub[i])
            return sub
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"

    @classmethod
    def multiplication(cls, list_mul):
        """calculating multiply function"""
        try:
            mul = 1
            for i in list_mul:
                mul = mul * float(i)
            return mul
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"

    @classmethod
    def division(cls, list_div):
        """calculating divide function"""
        try:
            div = float(list_div[0])
            for i in range(1,len(list_div)):
                div = div / float(list_div[i])
            return div
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"
        except ZeroDivisionError as ex:
            print("ZeroDivisionError")
            logging.error(ex)
            return "Enter a number greater than zero"
