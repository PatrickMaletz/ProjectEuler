from problemClass import Problem
import MathModule as MM
import solutions
import problems

def main():
    solve_all_problems = False
    solve_problem_num = 4

    all_problems = problems.init_problems()
    all_solutions = solutions.init_solutions()


    if solve_all_problems:
        for count, problem in enumerate(all_problems):
            try:
                all_problems[count].answer = all_solutions[count](problem.input)
                print("Problem #",problem.number,"\n",problem.description)
                print("The answer to problem ",problem.number," is: ", problem.answer)
            except:
                print("Problem #",problem.number,"\n",problem.description)
                print("This problem has not been solved yet.")
                
    print(MM.factorise(60).sort())

main()   





