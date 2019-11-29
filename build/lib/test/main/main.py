<<<<<<< HEAD
"""main function for testing"""
from test.driver.scientific_calc_test import ScientificCalcTest
import unittest

if __name__ == '__main__':
    TEST_OBJ = ScientificCalcTest()
=======
"""This module is used to create the object for the test class and calls it"""
import unittest
from test.driver.scientific_calc_test import ScientificCalcTest

if __name__ == '__main__':
    TESTCLASS_OBJ = ScientificCalcTest()
>>>>>>> b405f71bbc91cc713782c97c443adea95cbeff2e
    unittest.main()
