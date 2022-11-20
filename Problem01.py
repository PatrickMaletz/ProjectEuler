from problemClass import Problem
import MathModule as MM


def main():
    problem_num = 1
    problem_description = """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. \n
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."""
    problem_input = 1000
    
    Problem01 = Problem(problem_num,problem_description, problem_input)
    
    Problem01.answer = solve(problem_input)
    print(Problem01.answer)



def solve(problem_input):
    multiple_sum = 0
    for x in range(problem_input):
        if MM.multiple_of_n(x,3) or MM.multiple_of_n(x,5):
            multiple_sum += x

    return multiple_sum

main()