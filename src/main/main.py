from src.driver import ScientificCalc as a
import sys


def main():
    number = (sys.argv[1])
    t=a.scientific_calc()
    res = t.cube_root(number)
    print(res)
