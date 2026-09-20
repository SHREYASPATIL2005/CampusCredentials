def factorial(number):
    """Return number! for a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is undefined for negative numbers")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


print(factorial(5))
