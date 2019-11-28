"""This module is going to calculate ten power x"""
import logging
logging.basicConfig(filename='logger_file.log', level=logging.ERROR,
                    format='%(asctime)s : %(levelname)s : %(message)s : %(lineno)s', filemode='w')


class ScientificCalc:
    """This class is used to calculate the scientific operation ten power x"""
    @classmethod
    def cal_power_ten(cls, pow_value):
        """This function is used to calculate ten power x value"""
        try:
            cls.answer = 10**float(pow_value)
            return cls.answer
        except ValueError as value_error:
            logging.error(value_error)
            raise ValueError