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
        if method_name[0] == 'sine_h':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power = method_name[1]
            print(obj_power.sine_h(power))
        else:
            raise MethodNotFoundException

    except IndexError as index:
        print(index)
        logging.exception(index)

    except UnnecessaryParameterException as parameter:
        logging.exception(parameter)

    except MethodNotFoundException as parameter:
        logging.exception(parameter)

# import sys
# from src.driver.scientific_calc import ScientificCalc
#
#
#
# def main():
#     num = float(sys.argv[1])
#     obj=ScientificCalc()
#     res = obj.sine_h(num)
#     print(res)