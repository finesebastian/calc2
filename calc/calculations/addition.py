"""Imports Calculation"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """This is the addition class, it returns the sum of its values"""
    def get_result(self):
        """Returns the result of summing value a and value b"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
