'''degree to radians'''
import math
import logging
logging.basicConfig(filename="ScientificCalculatorLog.log", level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='w')


class ScientificCalc:
    '''function to convert a number to radians'''
    def __init__(self):
        self.degree = 0
        self.radian = 0

    @classmethod
    def rad(cls, angle):
        '''calculate radians'''

        try:
            cls.degree = float(angle)
            constpi = math.pi
            cls.radian = cls.degree * (constpi / 180)
            return cls.radian
        except ValueError as ex:
            logging.error(ex)
            return "Value Error"
