"""main.py to call the unittest case Class"""
import unittest

from test.driver.scientific_calc_test import ScientificCalcTest


if __name__ == "__main__":
    TESTCLASS_OBJ = ScientificCalcTest()
    unittest.main()
