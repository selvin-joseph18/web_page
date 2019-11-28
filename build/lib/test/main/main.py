"""This module is used to create the object for the test class and calls it"""
from test.driver.scientific_calc_test import ScientificCalcTest
import unittest

if __name__ == '__main__':
    TESTCLASS_OBJ = ScientificCalcTest()
    unittest.main()
