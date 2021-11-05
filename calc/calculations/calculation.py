"""Calculation Class"""
class Calculation:
    # pylint: disable=too-few-public-methods
    """Returns no values, but accepts tuple to generate values float list"""
    def __init__(self, values: tuple):
        """Initiates values as a list of floats"""
        self.values = Calculation.convert_args_to_list_float(values)

    @classmethod
    def create(cls, values: tuple):
        """Factory method"""
        return cls(values)

    @staticmethod
    def convert_args_to_list_float (values):
        """Generates a list of floats for tuple input"""
        list_values_float =[]
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
