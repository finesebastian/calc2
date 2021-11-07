"""Imports Calculation"""
from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """This is the subtraction Class"""
    def get_result(self):
        """Returns the difference of value_b from value_a"""
        sum_of_values = self.values[0]
        for value in self.values[1:len(self.values)]:
            sum_of_values = sum_of_values - value
        return sum_of_values
