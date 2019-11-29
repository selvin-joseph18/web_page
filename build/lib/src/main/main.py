<<<<<<< HEAD
"""The main function to call cosh program """
import argparse
from src.driver.scientific_calc import ScientificCalc


def main():
    """get input and call the function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', type=str, required=True, nargs='+')
    args = parser.parse_args()
    arguments = args.function
    method_name = arguments[0]
    number = arguments[1]
    calc = ScientificCalc()
    if method_name == 'trig_cosh':

        res = calc.trig_cosh(number)
        print(res)
    else:
        print("method not found")
=======
"""This module is used for main method"""
from __future__ import print_function
import argparse
import logging
from src.exception.unnecessary_parameter_exception import UnnecessaryParameterException
from src.driver.scientific_calc import ScientificCalc
from src.exception.method_not_found_exception import MethodNotFoundException

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
        elif method_name[0] == '10_power_x':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power_val = method_name[1]
            print(obj_power.cal_power_ten(power_val))
        elif method_name[0] == 'x_power_y':
            if len(method_name) > 3:
                raise UnnecessaryParameterException
            input_base = method_name[1]
            input_power = method_name[2]
            final_answer = obj_power.var_initialization(input_base, input_power)
            print(final_answer)
        elif method_name[0] == 'calculate_tanh':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            res = obj_power.calculate_tanh(method_name[1])
            print(res)
        else:
            raise MethodNotFoundException

    except IndexError as index:
        print(index)
        logging.exception(index)

    except UnnecessaryParameterException as parameter:
        logging.exception(parameter)

    except MethodNotFoundException as parameter:
        logging.exception(parameter)
>>>>>>> b405f71bbc91cc713782c97c443adea95cbeff2e
