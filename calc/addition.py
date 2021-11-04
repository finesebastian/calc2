"""Imports Calculation"""
from calc.calculation import Calculation

class Addition(Calculation):
    """This is the addition class, it returns the sum of its values"""
    def get_result(self):
        """Returns the result of summing value a and value b"""
        return self.value_a + self.value_b
