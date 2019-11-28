"""This module is used for main method"""
from __future__ import print_function
import argparse
import logging
from src.driver.scientific_calc import ScientificCalc
logging.basicConfig(filename='logger_file.log', level=logging.ERROR,
                    format='%(asctime)s : %(levelname)s : %(message)s : %(lineno)s', filemode='w')


def main():
    """This main method is used to call the scientific operation 10 power x"""
    try:
        power_x_obj = ScientificCalc()
        parser = argparse.ArgumentParser()
        parser.add_argument('--function', type=str, required=True, nargs='+')
        args = parser.parse_args()
        method_name = args.function
        if method_name[0] == '10_power_x':
            power_val = method_name[1]
            print(power_x_obj.cal_power_ten(power_val))

    except ValueError as value_error:
        logging.error(value_error)
        print('Error has occured')