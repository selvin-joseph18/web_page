<<<<<<< HEAD
from test.driver.ScientificCalc_Test import ScientificCalc_Test
import unittest

if __name__ == '__main__':
    test_obj = ScientificCalc_Test()
    unittest.main()
=======
"""This module is used to create the object for the test class and calls it"""
import unittest
from test.driver.scientific_calc_test import ScientificCalcTest

if __name__ == '__main__':
    TESTCLASS_OBJ = ScientificCalcTest()
    unittest.main()
>>>>>>> 5cbf5afd1f7818e7929d0c0b88bcc50f1435e5a8
