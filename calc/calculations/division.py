"""Imports Calculation"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """This is the division class"""
    def get_result(self):
        """Return the quotient of value_a and value_b"""
        return self.value_a / self.value_b
