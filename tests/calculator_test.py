"""Testing the Calculator"""
import pytest

from calculator.calculator import Calculator

@pytest.fixture
def clear_history_fixture():
    """"Creates fixture for clearing history after each test"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.clear_history()

def test_calculator_add(clear_history_fixture):
    """Testing the Add function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1,2) == 3

def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_number(3,4) == -1

def test_calculator_multiplication(clear_history_fixture):
    """ Testing the Multiplication method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiple_number(2,3) == 6

def test_calculator_division(clear_history_fixture):
    """ Testing the division method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_number(8,4) == 2

def test_calculator_division_by_zero(clear_history_fixture):
    """ Testing the division by zero try/except catch of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(Calculator.divide_number(1,0), ArithmeticError)

def test_calculator_get_last_history(clear_history_fixture):
    """ Testing the get_last history function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_last_calculation_result() == 4

def test_calculator_get_first_history(clear_history_fixture):
    """ Testing the get_last history function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_first_calculation_result() == 3

def test_calculator_get_last_calculation_history(clear_history_fixture):
    """ Testing the get_last history function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_last_calculation() == Calculator.history[1]

def test_calculator_complete(clear_history_fixture):
    """Testing each section of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.clear_history() == 0
    assert Calculator.add_number(1,2) == 3
    assert Calculator.subtract_number(2,1) == 1
    assert Calculator.count_history() == 2
    assert Calculator.history[0].get_result() == 3
    assert Calculator.history[1].get_result() == 1
