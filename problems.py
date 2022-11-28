from problemClass import Problem
def init_problems():
    return

def problem01():

    problem_num = 1
    problem_description = """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. \n
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."""

    problem_input = 1000
    
    Problem01 = Problem(problem_num,problem_description, problem_input)
    return Problem01

def problem02():
    problem_num = 2
    problem_description = """

    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

    """
    problem_input = 4_000_000
    
    Problem02 = Problem(problem_num,problem_description, problem_input)

    return Problem02
    
def problem03():

    problem_num = 3
    problem_description = """

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    """
    problem_input = 600851475143
    
    Problem02 = Problem(problem_num,problem_description, problem_input)

    return Problem02



