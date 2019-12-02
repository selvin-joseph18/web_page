'''
Python program to calculate Cosine of an angle
'''
import math
import logging
logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')

class ScientificCalc:

    @classmethod
    def calculate_cos(cls,angle):
        '''
        Function to calculate Cosine of an angle
         '''
        try:
            cls.result = math.cos(angle)
            return cls.result
        except TypeError as type_error:
            logging.error(type_error)
