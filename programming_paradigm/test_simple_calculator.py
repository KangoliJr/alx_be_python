import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(4, 3), 7)
        self.assertEqual(self.calc.add(-4, 3), -1)
        self.assertEqual(self.calc.add(-4, -3), -7)
        self.assertEqual(self.calc.add(0, 3), 3)
        self.assertEqual(self.calc.add(4.2, 3.8), 8.0)
        self.assertEqual(self.calc.add(4, -3), 1)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(-4, 3), -7)
        self.assertEqual(self.calc.subtract(-4, -3), -1)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertAlmostEqual(self.calc.subtract(4.5, 3.2), 1.3)
        self.assertEqual(self.calc.subtract(4, -3), 7)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 2), 20) 
        self.assertEqual(self.calc.multiply(-10, 3), -30) 
        self.assertEqual(self.calc.multiply(-12, -3), 36) 
        self.assertEqual(self.calc.multiply(0, 7), 0) 
        self.assertEqual(self.calc.multiply(2.5, 2.5), 6.25) 
        self.assertEqual(self.calc.multiply(8, -5), -40)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(30, 3), 10.0) 
        self.assertEqual(self.calc.divide(-18, 3), -6.0) 
      
        self.assertEqual(self.calc.divide(-81, -9), 9.0) 
        self.assertEqual(self.calc.divide(15, 2), 7.5) 
        self.assertEqual(self.calc.divide(0, 2), 0.0)
        
    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(45, 0)) 
        self.assertIsNone(self.calc.divide(0, 0)) 
        
if __name__ == '__main__':
    unittest.main()