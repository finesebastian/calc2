""" This imports the calculation class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(tuple_of_numbers: tuple):
        """ Instantiating Addition object and passing value a and b to the constructor"""
        # Factory create method to return an instance of the class
        calculation = Addition.create(tuple_of_numbers)
        # -1 returns the last item added to a list
        return calculation.get_result()

    @staticmethod
    def subtract_number(tuple_of_numbers: tuple):
        """ subtract number from result"""
        calculation = Subtraction.create(tuple_of_numbers)
        return calculation.get_result()

    @staticmethod
    def multiple_number(tuple_of_numbers: tuple):
        """ multiply number from result"""
        calculation = Multiplication.create(tuple_of_numbers)
        return calculation.get_result()

    @staticmethod
    def divide_number(tuple_of_numbers: tuple):
        """ divide number from result"""
        calculation = Division.create(tuple_of_numbers)
        return  calculation.get_result()
