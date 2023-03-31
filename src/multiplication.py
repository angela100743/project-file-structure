import src.addition

def perform_operation(multiplier, multiplicand):
    result = 0
    for _ in range(multiplier):
        result = src.addition.perform_operation(result, multiplicand)
    return result