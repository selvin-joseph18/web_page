import sys
# import src.driver.ScientificCalc
from src.driver.ScientificCalc import ScientificCalc


def main():

    try:
        n = sys.argv[1]
        class_obj = ScientificCalc()
        print class_obj.factorial_number(int(n))
    except ValueError:
        print 'Enter a number'
    except IndexError:
        print 'enter number aaa'
