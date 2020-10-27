# python3
import random

def max_pairwise_product(numbers):
    sorted_list = []
    sorted_list = sorted(numbers)

    return sorted_list[-1] * sorted_list[-2]

def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    while True:
        #STRESS TEST
        # n = random.randint(1,100) + 2
        # input_numbers = [random.randint(1,100) for i in range(n)]
        # slow_solution = max_pairwise_product_slow(input_numbers)
        # fast_solution = max_pairwise_product(input_numbers)

        # print(f"input n is {n} while input numbers are {input_numbers}")
        # print(f"slow solution is {slow_solution} while fast solution is {fast_solution}")
        # if(slow_solution == fast_solution) : print('OK')
        # else: break

        #DEFAULT IMPLEMENTATION
        input_n = int(input())
        input_numbers = [int(x) for x in input().split()]
        print(max_pairwise_product(input_numbers))
