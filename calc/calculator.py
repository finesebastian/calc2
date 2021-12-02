""" This imports the calculation class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(*args):
        """ Instantiating Addition object and passing value a and b to the constructor"""
        # Factory create method to return an instance of the class
        calculation = Addition.create(args)
        # -1 returns the last item added to a list
        return calculation.get_result()

    @staticmethod
    def subtract_number(*args):
        """ subtract number from result"""
        calculation = Subtraction.create(args)
        return calculation.get_result()

    @staticmethod
    def multiple_number(*args):
        """ multiply number from result"""
        calculation = Multiplication.create(args)
        return calculation.get_result()

    @staticmethod
    def divide_number(*args):
        """ divide number from result"""
        calculation = Division.create(args)
        return  calculation.get_result()
