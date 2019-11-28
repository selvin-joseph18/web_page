"""This module is used to create the ohect for the test class and calls it"""
from test.driver.scientific_calc_test import MyTestCase
import unittest

if __name__ == '__main__':
    TEST_CLASS = MyTestCase()
    unittest.main()