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
