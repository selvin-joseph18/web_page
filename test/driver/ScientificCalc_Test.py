"""import module"""
import unittest
from src.driver.ScientificCalc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):

    def test_logarithm(self):
        """test_against_positive_input"""
        res = ScientificCalc()
        self.assertEqual(res.logarithm(100000), 5.0)

    def test_logarithm2(self):
        """test_type_of_variable"""
        res = ScientificCalc()
        self.assertTrue(type(res.logarithm(10)), int)

    def test_logarithm3(self):
        """test_for_negative_number"""
        res = ScientificCalc()
        self.assertEquals(res.logarithm(-10),'ValueError')

    def test_logarithm4(self):
        """test_for_type_of_variable"""
        res = ScientificCalc()
        self.assertEquals(res.logarithm("prasad"), 'TypeError')


if __name__ == '__main__':
    unittest.main()

