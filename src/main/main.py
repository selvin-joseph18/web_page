'''main function'''
import argparse
from src.driver.scientific_calc import ScientificCalc


def main():
    '''main function'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', type=str, required=True, nargs='+')
    args = parser.parse_args()
    arguments = args.function
    method_name = arguments[0]
    angle = arguments[1]
    calc = ScientificCalc()
    if method_name == 'rad':
        res = calc.rad(angle)
        print(res)
    else:
        print("method not found")
