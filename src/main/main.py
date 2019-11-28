"""This module is used for main method"""
from __future__ import print_function
import argparse
import logging
from src.exception.unnecessary_parameter_exception import UnnecessaryParameterException
from src.driver.scientific_calc import ScientificCalc

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')

def main():
    """This main function is used to get input from user and call the scientific calculator
    functions, create object for scientific_calc class, passing parameters using Command Line
    and calling the method"""
    try:
        obj_power = ScientificCalc()
        parser = argparse.ArgumentParser()
        parser.add_argument('--function', type=str, required=True, nargs='+')
        args = parser.parse_args()
        method_name = args.function
        if method_name[0] == 'e_power_x':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power = method_name[1]
            print(obj_power.exponential_func(power))
        if method_name[0] == '10_power_x':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power_val = method_name[1]
            print(obj_power.cal_power_ten(power_val))
        if method_name[0] == 'x_power_y':
            if len(method_name) > 3:
                raise UnnecessaryParameterException
            input_base = method_name[1]
            input_power = method_name[2]
            final_answer = obj_power.var_initialization(input_base, input_power)
            print(final_answer)

    except IndexError as index:
        print(index)
        logging.exception(index)

    except UnnecessaryParameterException as parameter:
        logging.exception(parameter)
