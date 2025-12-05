import unittest
from src.calculator import Calculator

class TestCalculatorUnit(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
