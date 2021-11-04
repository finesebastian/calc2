"""This class tests calculations functionality"""
import pytest

from calculator.calculations import Calculations

@pytest.fixture
def clear_history_fixture():
    """"Creates fixture for clearing history after each test"""
    Calculator.clear_history()

def test_get_calculation(clear_history_fixture):
