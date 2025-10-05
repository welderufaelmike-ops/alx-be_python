
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
           
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(9, 4), 5)
        self.assertEqual(self.calc.subtract(-18, 10), -28)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(9, 3), 27)
        self.assertEqual(self.calc.multiply(10, 5), 50)
   
    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(30, 6), 5)
        self.assertEqual(self.calc.divide(3, 1), 3)

if __name__ == '__main__':
    unittest.main()


