from problemClass import Problem
import MathModule as MM


def solve01(problem_input):
    multiple_sum = 0
    for x in range(problem_input):
        if MM.multiple_of_n(x,3) or MM.multiple_of_n(x,5):
            multiple_sum += x

    return multiple_sum

def solve02(problem_input):
    previous_sum = 1
    next_sum = 0
    sum = 1
    total = 0
    while sum < problem_input:
        if MM.isEven(sum):
            total += sum

        next_sum = MM.nextFibonacci(sum,previous_sum)
        previous_sum = sum
        sum = next_sum

    return total
        


