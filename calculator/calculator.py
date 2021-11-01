""" This is the increment function"""

class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        return value_a + value_b

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        return value_a - value_b

    @staticmethod
    def multiple_number(value_a, value_b):
        """ multiply number from result"""
        return value_a * value_b

    @staticmethod
    def divide_number(value_a, value_b):
        """ divide number from result"""
        try:
            return value_a / value_b
        except ArithmeticError:
            return ArithmeticError('Division by Zero')

    @staticmethod
    def exp_number(value_a, value_b):
        """ Exponentiate Value_A by Value_B"""
        return value_a ** value_b
