"""Testing the Calculator"""
from calculator.calculator import Calculator

def test_calculator_add():
    """Testing the subtract method of the calculator"""
    num_tuple = (3,4)
    assert Calculator.add_number(num_tuple) == 7

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    num_tuple = (3, 4)
    assert Calculator.subtract_number(num_tuple) == -1

def test_calculator_multiplication():
    """ Testing the Multiplication method of the calculator"""
    num_tuple = (2, 3)
    assert Calculator.multiple_number(num_tuple) == 6

def test_calculator_division():
    """ Testing the division method of the calculator"""
    num_tuple = (8, 4)
    assert Calculator.divide_number(num_tuple) == 2

def test_calculator_division_by_zero():
    """ Testing the division by zero try/except catch of the calculator"""
    num_tuple = (1, 0)
    assert isinstance(Calculator.divide_number(num_tuple), ArithmeticError)
