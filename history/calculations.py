"""Calculation History Class"""

class Calculations:
    """This is the calculations class"""
    history=[]
    #pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """Clears History List"""
        Calculations.history.clear()
        return True

    @staticmethod
    def get_last_calculation_result():
        """ Returns last calculated value added to history list"""
        last_calculation_object = Calculations.get_last_calculation()
        return last_calculation_object.get_result()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Adds calculation to history list"""
        Calculations.add_history(calculation)

    @staticmethod
    def get_calculation(num):
        """ Returns calculation object at num"""
        return Calculations.history[num]

    @staticmethod
    def get_calculation_result(num):
        """ Returns calculation object result at num"""
        return Calculations.get_calculation(num).get_result()

    @staticmethod
    def get_last_calculation():
        """ Returns the last calculation object"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """ Returns the first calculation object"""
        return Calculations.history[0]

    @staticmethod
    def get_first_calculation_result():
        """ Returns first calculated value added to history list"""
        first_calculation_object = Calculations.get_first_calculation()
        return first_calculation_object.get_result()

    @staticmethod
    def count_history():
        """ Returns the length of the history list"""
        return len(Calculations.history)

    @staticmethod
    def add_history(calculation):
        """ Adds calculation to history"""
        return Calculations.history.append(calculation)
