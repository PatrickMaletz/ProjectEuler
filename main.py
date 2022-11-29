from problemClass import Problem
import MathModule as MM
import solutions
import problems

def main():
    solve_all_problems = False
    solve_problem_num = 3

    all_problems = problems.init_problems()
    all_solutions = solutions.init_solutions()


    if solve_all_problems:
        for count, problem in enumerate(all_problems):
            all_problems[count].answer = all_solutions[count](problem.input)
            print("Problem #",problem.number,"\n",problem.description)
            print("The answer to problem ",problem.number," is: ", problem.answer)

    print(MM.is_palindrome(10101))


main()   





