def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    # Example usage:
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")
