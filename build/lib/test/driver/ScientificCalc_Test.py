import unittest
from src.driver.scientific_calc import ScientificCalc
class MyTestCase(unittest.TestCase):
    """test case class"""
    def test_1(self):
        """positive value"""
        obj1=ScientificCalc()
        self.assertEqual(obj1.sine_h(30), 5343129467557.554)

    def test_2(self):
        """negative value"""
        obj2=ScientificCalc()
        self.assertEqual(obj2.sine_h(-1), -1.1752001556866842)

    def test_3(self):
        """zero"""
        obj3=ScientificCalc()

        self.assertEqual(obj3.sine_h(0), 0)

if __name__ == '__main__':
    unittest.main()
