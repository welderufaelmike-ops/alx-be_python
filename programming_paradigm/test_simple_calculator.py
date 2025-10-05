
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
        # Add more assertions to thoroughly test the add method.
    def test_substract(self):
        """Test the substract method."""
        self.assertEqual(self.calc.subtract(9 ,4), 5)
    
    def test_divide(self):
        """"Test the divide method."""
        self.assertEqual(self.calc.divide(30 , 6) ,5)
        self.assertEqual(self.calc.divide(3, 0), None)