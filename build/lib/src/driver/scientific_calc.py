"""simple calculator to find tanh"""
import math
import logging

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')


class ScientificCalc:
    """A class to calculate tanh """
    def __init__(self):
        self.angle = 0
        self.tanhx = 0

    @classmethod
    def calculate_tanh(cls, angle):
        """A method to calculate tanh"""
        try:
            cls.angle = angle
            cls.angle = float(cls.angle)
            exponential = math.e
            coshx = ((exponential ** cls.angle) + (exponential ** -cls.angle))
            sinhx = ((exponential ** cls.angle) - (exponential ** -cls.angle))
            cls.tanhx = sinhx / coshx
            return cls.tanhx
        except ValueError as error:
            logging.exception(error)
            return "value error(enter a number)"
