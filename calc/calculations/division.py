"""Imports Calculation"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """This is the division class"""
    def get_result(self):
        """Return the quotient of value_a and value_b"""
        sum_of_values = self.values[0]
        for value in self.values[1:len(self.values)]:
            try:
                sum_of_values =  sum_of_values / value
            except ArithmeticError:
                return ArithmeticError('Division by Zero')
        return sum_of_values
