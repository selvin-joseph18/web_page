from src.driver.ScientificCalc import ScientificCalc
import sys


def main():
    x = (sys.argv[1])
    res = ScientificCalc.one_by_x(x)
    print(res)
