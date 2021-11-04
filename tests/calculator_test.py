"""Testing the Calculator"""
import pytest

from calculator.calculator import Calculator

@pytest.fixture
def clear():
    """"Creates fixture for clearing history after each test"""
    Calculator.clear_history()

def test_calculator_add(clear):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3

def test_calculator_subtract(clear):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(3,4) == -1

def test_calculator_multiplication(clear):
    """ Testing the Multiplication method of the calculator"""
    assert Calculator.multiple_number(2,3) == 6

def test_calculator_division(clear):
    """ Testing the division method of the calculator"""
    assert Calculator.divide_number(8,4) == 2

def test_calculator_division_by_zero(clear):
    """ Testing the division by zero try/except catch of the calculator"""
    assert isinstance(Calculator.divide_number(1,0), ArithmeticError)

def test_calculator_complete(clear):
    """Testing each section of the calculator"""
    assert Calculator.clear_history() == 0
    assert Calculator.add_number(1,2) == 3
    assert Calculator.subtract_number(2,1) == 1
    assert Calculator.count_history() == 2
    assert Calculator.history[0].get_result() == 3
    assert Calculator.history[1].get_result() == 1
