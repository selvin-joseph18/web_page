"""main method for scientific_calc.py"""
import argparse
import logging
from src.driver.scientific_calc import ScientificCalc
from src.exception.unnecessary_parameter_exception import UnnecessaryParameterException
from src.exception.method_not_found_exception import MethodNotFoundException

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')


def main():
    """object creation for ScientificcCalc class and arguments are passed to compute result"""
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--function', type=str, required=True, nargs='+')
        args = parser.parse_args()
        arguments = args.function
        method_name = arguments[0]
        angle = arguments[1]
        calc = ScientificCalc()
        if method_name == 'calculate_tanh':
            if len(arguments) > 2:
                raise UnnecessaryParameterException
            res = calc.calculate_tanh(angle)
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
