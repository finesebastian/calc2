"""This class tests calculations functionality"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """"Creates fixture for clearing history after each test"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

@pytest.fixture
def add_calculation_fixture():
    """"Creates fixture for adding value to history for each test"""
    values = (1,2)
    Calculations.add_calculation_to_history(Addition(values))

def test_get_calc_index(clear_history_fixture, add_calculation_fixture):
    """Tests functionality of index calling history object"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1
    values = (2, 2)
    Calculations.add_calculation_to_history(Addition(values))
    assert Calculations.count_history() == 2
    assert Calculations.get_calculation(1) == Calculations.history[1]

def test_get_calc_index_result(clear_history_fixture, add_calculation_fixture):
    """Tests functionality of index result calling history object"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1
    values = (2, 2)
    Calculations.add_calculation_to_history(Addition(values))
    assert Calculations.count_history() == 2
    assert Calculations.get_calculation_result(1) == 4

def test_add_calculation(clear_history_fixture, add_calculation_fixture):
    """Tests functionality of adding calculation to history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_clear_history(clear_history_fixture, add_calculation_fixture):
    """Tests clear history function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0

def test_get_last_calc(clear_history_fixture, add_calculation_fixture):
    """Tests if last calculation object can be returned"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation() == Calculations.history[-1]

def test_get_last_calc_result(clear_history_fixture, add_calculation_fixture):
    """Tests if last calculation object result can be returned"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result() == 3

def test_get_first_calc(clear_history_fixture, add_calculation_fixture):
    """Tests if first calculation object can be returned"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation() == Calculations.history[0]

def test_get_first_calc_result(clear_history_fixture, add_calculation_fixture):
    """Tests if first calculation object result can be returned"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation_result() == 3
