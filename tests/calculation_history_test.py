"""This class tests calculations functionality"""
import pytest

from history.calculations import Calculations
from calculator.calculator import Calculator

@pytest.fixture
def clear_history_fixture():
    """"Creates fixture for clearing history after each test"""
    Calculations.clear_history()

