""" This is the increment function"""

def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1

class Calculator:
    """ This is the Calculator class"""

    result = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result
    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result
    def multiple_number(self,value_a,value_b):
        """ multiply number from result"""
        self.result = value_a * value_b
        return self.result
    def divide_number(self, value_a, value_b):
        """ divide number from result"""
        self.result = value_a / value_b
        return self.result
    def exp_number(self, value_a, value_b):
        """ Exponentiate Value_A by Value_B"""
        self.result = value_a ** value_b
        return self.result

    def multiply_numbers(self, value_a, value_b):
        """ multiply two numbers and get result"""
        self.result = value_a * value_b
        return self.result

