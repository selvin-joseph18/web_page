<<<<<<< HEAD
"""import module"""
=======
"""unit test case for square root"""

>>>>>>> b0886e731bbe124f7f8e6c655e3d02a0e8383af0
import unittest
from src.driver.ScientificCalc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):
<<<<<<< HEAD

    def test_logarithm(self):
        """test_against_positive_input"""
        res = ScientificCalc()
        self.assertEqual(res.logarithm(100000), 5.0)

    def test_logarithm2(self):
        """test_type_of_variable"""
        res = ScientificCalc()
        self.assertTrue(type(res.logarithm(10)), int)

    #
    # def test_logarithm3(self):
        """test_for_negative_number"""
    #     self.assertEquals('ValueError',src.driver.log.logarithm(-10))
    def test_logarithm4(self):
        """test_for_type_of_variable"""
        res = ScientificCalc()
        self.assertEquals(res.logarithm("prasad"), 'TypeError')
=======
    """ test cases"""
    def test_square_root_positive(self):
        """test case for positive value"""
        test=ScientificCalc()
        self.assertEqual(test.square_root(4), 2.0)

    def test_square_root_negative(self):
        """test case for negative value"""
        test =ScientificCalc()
        self.assertEqual(test.square_root(-8), complex(1.7319121124709868e-16 + 2.8284271247461903j))

    def test_square_root_string(self):
        """test case if we give string"""
        test = ScientificCalc()
        self.assertEqual(test.square_root("a"), "expecting integer value")
>>>>>>> b0886e731bbe124f7f8e6c655e3d02a0e8383af0


if __name__ == '__main__':
    unittest.main()
<<<<<<< HEAD

=======
>>>>>>> b0886e731bbe124f7f8e6c655e3d02a0e8383af0
