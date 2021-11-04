"""Calculation Class"""
class Calculation:
    # pylint: disable=too-few-public-methods
    """Returns no values, but accepts value a and value b within calculation object"""
    def __init__(self,value_a,value_b):
        """Initiates values a and b in calculation object"""
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create (cls, value_a, value_b):
        """Create methods turns values of value_a and value_b"""
        return cls(value_a, value_b)
