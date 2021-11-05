"""Imports Calculation"""
from calc.calculation import Calculation

class Division(Calculation):
    """This is the division class"""
    def get_result(self):
        """Return the product of value_a and value_b"""
        try:
            return self.value_a / self.value_b
        except ArithmeticError:
            return ArithmeticError('Division by Zero')
