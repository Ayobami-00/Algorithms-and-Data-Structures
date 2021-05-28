"""
Question : Given a decimal number i.e a number in base 10 return the binmary equivalent of the number

"""


def decimalToBinary(n):
    assert int(n) == n, "Value must be an integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))


print(decimalToBinary(10))
