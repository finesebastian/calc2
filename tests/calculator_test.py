"""Testing the Calculator"""
from calc.calculator import Calculator

def test_calculator_add():
    """Testing the subtract method of the calculator"""
    assert Calculator.add_number(3,4) == 7

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(3,4) == -1

def test_calculator_multiplication():
    """ Testing the Multiplication method of the calculator"""
    assert Calculator.multiple_number(2,3) == 6

def test_calculator_division():
    """ Testing the division method of the calculator"""
    assert Calculator.divide_number(8,4) == 2

def test_calculator_division_by_zero():
    """ Testing the division by zero try/except catch of the calculator"""
    assert isinstance(Calculator.divide_number(1,0), ArithmeticError)
