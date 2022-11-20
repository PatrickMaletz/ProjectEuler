from ..problemClass import Problem


def main():
    problem_num = 2
    problem_description = """

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
    problem_input = 1000
    
    Problem02 = Problem(problem_num,problem_description, problem_input)
    
    print(Problem02.description)


main()