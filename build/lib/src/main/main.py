import sys
import argparse
from src.driver.scientific_calc import ScientificCalc
from src.exception.unnecessary_parameter_exception import UnnecessaryParameterException



def main():
    obj_power = ScientificCalc()
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', type=str, required=True, nargs='+')
    args = parser.parse_args()
    method_name = args.function
    if method_name[0] == 'addition':
        if len(method_name) > 3:
            raise UnnecessaryParameterException
        input1 = method_name[1]
        input2 = method_name[2]
        print(obj_power.addition(input1, input2))

    if method_name[0] == 'subtraction':
        if len(method_name) > 3:
            raise UnnecessaryParameterException
        input1 = method_name[1]
        input2 = method_name[2]
        print(obj_power.subtraction(input1, input2))

    if method_name[0] == 'multiplication':
        if len(method_name) > 3:
            raise UnnecessaryParameterException
        input1 = method_name[1]
        input2 = method_name[2]
        print(obj_power.multiplication(input1, input2))

    if method_name[0] == 'division':
        if len(method_name) > 3:
            raise UnnecessaryParameterException
        input1 = method_name[1]
        input2 = method_name[2]
        print(obj_power.division(input1, input2))
