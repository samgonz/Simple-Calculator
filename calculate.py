"""Computes basic math operations determining on the operator passed in.
"""
def calculate(first_number, operator, last_number):
    """Computes basic math operations

    Args:
        first_number (float): first number the user inputs
        operator (string): The operator (+, -, *, /)
        last_number (float): last number the user inputs

    Returns:
        Float: The result of the math operation performed.
    """    
    if operator == '+':
        return first_number + last_number
    if operator == '*':
        return first_number * last_number
    if operator == '/':
        return first_number / last_number
    if operator == '-':
        return first_number - last_number
