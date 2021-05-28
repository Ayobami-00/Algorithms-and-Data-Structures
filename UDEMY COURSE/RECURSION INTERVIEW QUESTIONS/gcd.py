"""
Question : Given two numbers, find the greatest common divisors or highest common factors of the numbers

"""


def gcd(a, b):
    assert int(a) == a and int(b) == b, "Value(s) must be integers"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(48, 18))
