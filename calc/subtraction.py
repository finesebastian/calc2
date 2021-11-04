"""Imports Calculation"""
from calc.calculation import Calculation

class Subtraction(Calculation):
    """This is the subtraction Class"""
    def get_result(self):
        """Returns the difference of value_b from value_a"""
        return self.value_a - self.value_b
