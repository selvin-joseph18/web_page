import logging
logging.basicConfig(level=logging.exception('Exception occured'))

"""MODULE IS USED TO FIND SINH VALUE"""


class ScientificCalc:
    def __init__(self):
        self.sinh_of_x=0

    @classmethod
    def sine_h(cls, x_value):
        """formula for finding sin"""
        exp_value = 2.71828
        try:
            cls.sinh_of_x = (exp_value ** x_value - exp_value ** (- x_value)) / 2
            return cls.sinh_of_x

        except Exception as e:
                print("Exception handled", e)
                logging.error('Error logged')
