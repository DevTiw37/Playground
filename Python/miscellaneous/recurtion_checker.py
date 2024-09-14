def divide_and_print(numerator, denominator):
    """
    Divides the numerator by the denominator and prints the digits of the result.

    Args:
        numerator: The numerator of the division.
        denominator: The denominator of the division.
    """

    if denominator == 0:
        print("Error: Division by zero is not allowed.")
        return

    quotient = numerator // denominator
    remainder = numerator % denominator

    print(quotient, end=" ")

    while remainder != 0:
        remainder *= 10
        quotient = remainder // denominator
        print(quotient, end=" ")
        remainder %= denominator

divide_and_print(22, 7)