""" This imports the calculation class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(value_a, value_b):
        """ Instantiating Addition object and passing value a and b to the constructor"""
        # Factory create method to return an instance of the class
        Calculator.add_calculation_to_history(Addition.create(value_a,value_b))
        # -1 returns the last item added to a list
        return Calculator.get_last_calculation_result()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        Calculator.add_calculation_to_history(Subtraction.create(value_a, value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def multiple_number(value_a, value_b):
        """ multiply number from result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def divide_number(value_a, value_b):
        """ divide number from result"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        try:
            return Calculator.get_last_calculation_result()
        except ArithmeticError:
            return ArithmeticError('Division by Zero')
