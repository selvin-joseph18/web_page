from src.driver.scientific_calc import  ScientificCalc
import sys


def main():
    scientificcalc =  ScientificCalc()
    angle = float(sys.argv[1])
    print( scientificcalc.calculate_cos(angle))