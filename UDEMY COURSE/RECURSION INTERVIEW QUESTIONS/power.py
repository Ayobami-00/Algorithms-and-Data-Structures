"""
Question : Given a number, find the power to the n-th(exp) value

"""


def power(number, exp):
    assert exp >= 0 and int(exp) == exp, "Exponent value must be a positive integer"
    if exp == 0:
        return 1
    if exp == 1:
        return number
    return number * power(number, exp-1)


print(power(2, 10))
