""" This imports the calculation class"""
from history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def get_calculator_result():
        """Returns last calculation object result"""
        return Calculations.get_last_calculation_result()

    @staticmethod
    def add_number(tuple_of_numbers: tuple):
        """ Instantiating Addition object and passing tuple through Calculations"""
        Calculations.add_addition_calculation_to_history(tuple_of_numbers)

    @staticmethod
    def subtract_number(tuple_of_numbers: tuple):
        """ subtract number from result"""
        Calculations.add_subtraction_calculation_to_history(tuple_of_numbers)

    @staticmethod
    def multiple_number(tuple_of_numbers: tuple):
        """ multiply number from result"""
        Calculations.add_multiplication_calculation_to_history(tuple_of_numbers)

    @staticmethod
    def divide_number(tuple_of_numbers: tuple):
        """ divide number from result"""
        Calculations.add_division_calculation_to_history(tuple_of_numbers)
