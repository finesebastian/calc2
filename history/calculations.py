"""Calculation History Class"""

class Calculations:
    history=[]
    #pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """Clears History List"""
        history.clear()
        return True

    @staticmethod
    def get_last_calculation_result():
        """ Returns last calculated value added to history list"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Adds calculation to history list"""
        Calculator.history.append(calculation)

    @staticmethod
    def get_last_calculation():
        """ Returns the last calculation object"""
        return Calculator.history[-1]

    @staticmethod
    def count_history():
        """ Returns the length of the history list"""
        return len(Calculator.history)

