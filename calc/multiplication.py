"""Imports Calculation"""
from calc.calculation import Calculation

class Multiplication(Calculation):
    """This is the multiplication class"""
    def get_result(self):
        """Return the product of value_a and value_b"""
        return self.value_a * self.value_b
