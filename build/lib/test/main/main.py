"""main.py to call the unittest case Class"""
from test.driver.scientific_calc_test import ScientificCalcTest
import unittest

if __name__ == '__main__':
    TESTCLASS_OBJ = ScientificCalcTest()
    unittest.main()
