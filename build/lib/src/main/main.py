"""This module is used to write main function"""
from src.driver.scientific_calc import ScientificCalc
import argparse


def main():
    """This main function is used to get input from user and call the exponential_function"""

    obj_exp = ScientificCalc()
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', type=str, required=True, nargs='+')
    args = parser.parse_args()
    method_name = args.function
    if method_name[0] == 'e_power_x':
        power = method_name[1]
        print(obj_exp.exponential_func(power))
