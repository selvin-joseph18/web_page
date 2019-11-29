
import sys
from src.driver.scientific_calc import ScientificCalc



def main():
    num = float(sys.argv[1])
    obj=ScientificCalc()
    res = obj.sine_h(num)
    print(res)