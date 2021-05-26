"""
Question : Find the factorial of a positive integer using recursion

"""


def factorial(n):
    assert n >= 0 and int(n) == n, "Value must be a Positive Integer"
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))
# print(factorial(-1))



"""
Question : Find the n-th fibonacci number of a positive integer using recursion

"""

def fibonacci(n):
    assert n >= 0 and int(n) == n , "Value must be a Positive Integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
# print(fibonacci(-1))