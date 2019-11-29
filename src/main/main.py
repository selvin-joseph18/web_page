from src.driver.ScientificCalc import ScientificCalc

import sys


def main():
    x = (sys.argv[1])
    res = ScientificCalc.square_root(x)
    print(res)
