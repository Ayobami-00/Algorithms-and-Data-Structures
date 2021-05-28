"""
Question : Given a positive integer, find the sum of it's digits.

"""


def sumOfDigits(number):
    assert number >= 0 and int(
        number) == number, "Value must be a positive integer"

    if number == 0:
        return 0
    else:
        return (number % 10) + sumOfDigits(number//10)


print(sumOfDigits(1024))
