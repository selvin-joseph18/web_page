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
        add_list = []
        for key in range(1,len(method_name)):
            add_list.append(method_name[key])
        print(obj_power.addition(add_list))

    elif method_name[0] == 'subtraction':
        sub_list = []
        for key in range(1, len(method_name)):
            sub_list.append(method_name[key])
        print(obj_power.subtraction(sub_list))

    elif method_name[0] == 'multiplication':
        mul_list = []
        for key in range(1, len(method_name)):
            mul_list.append(method_name[key])
        print(obj_power.multiplication(mul_list))

    elif method_name[0] == 'division':
        div_list = []
        for key in range(1, len(method_name)):
            div_list.append(method_name[key])
        print(obj_power.division(div_list))
