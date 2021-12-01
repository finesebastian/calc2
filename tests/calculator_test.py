"""Testing the Calculator"""
from calculator.calculator import Calculator

def test_calculator_add():
    """Testing the subtract method of the calculator"""
    num_tuple = (3, 4)
    Calculator.add_number(num_tuple)
    assert Calculator.get_calculator_result() == 7

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    #Arrange a sample set of numbers within a tuple to be evaluated by the calculator.
    num_tuple = (3, 4)
    #Act by calling the subtraction function of the calculator
    Calculator.subtract_number(num_tuple)
    #Assert the operation (subtraction) results in the correct result: -1
    assert Calculator.get_calculator_result() == -1

def test_calculator_multiplication():
    """ Testing the Multiplication method of the calculator"""
    num_tuple = (2, 4)
    Calculator.multiple_number(num_tuple)
    assert Calculator.get_calculator_result() == 8

def test_calculator_division():
    """ Testing the division method of the calculator"""
    num_tuple = (8, 4)
    Calculator.divide_number(num_tuple)
    assert Calculator.get_calculator_result() == 2

def test_calculator_division_by_zero():
    """ Testing the division by zero try/except catch of the calculator"""
    num_tuple = (1, 0)
    Calculator.divide_number(num_tuple)
    assert isinstance(Calculator.get_calculator_result(), ArithmeticError)
