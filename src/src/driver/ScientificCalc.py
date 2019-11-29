"""import math module"""

import logging

file_name = 'new_file.log'
logging.basicConfig(filename=file_name, level=logging.ERROR,
                    format='%(asctime)s %(message)s',
                    filemode='w')


class ScientificCalc:
    def __init__(self, number):
        self.number = number

    @classmethod
    def factorial_number(self, number):
        """printing fact of a number"""
        try:
            if number >= 0:

                if number == 0 or number == 1:
                    return 1
                else:

                    return number * self.factorial_number(number - 1)
            else:
                raise ValueError

        except ValueError as v:
            logging.error(v.message)
            print 'Enter positive Integer', v
        except TypeError as t:
            logging.error(t.message)
            print 'enter a Integer', t


