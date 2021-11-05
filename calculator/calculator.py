""" This imports the calculation class"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.division import Division
from calc.multiplication import Multiplication


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def count_history():
        """ Returns the length of the history list"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Adds calculation to history list"""
        Calculator.history.append(calculation)

    @staticmethod
    def get_last_calculation():
        """ Returns the last calculation object"""
        return Calculator.history[-1]

    @staticmethod
    def get_last_calculation_result():
        """ Returns last calculated value added to history list"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def get_first_calculation_result():
        """ Returns the first stored result in history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def clear_history():
        """Clears History List"""
        Calculator.history.clear()
        return Calculator.count_history()

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
        return Calculator.get_last_calculation_result()
