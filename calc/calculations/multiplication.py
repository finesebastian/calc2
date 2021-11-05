"""Imports Calculation"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """This is the multiplication class"""
    def get_result(self):
        """Return the product of value_a and value_b"""
        sum_of_values = 1.0
        for value in self.values:
            sum_of_values = sum_of_values * value
        return sum_of_values
