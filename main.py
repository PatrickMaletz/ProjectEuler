import problems
import solutions
def main():
    solve_all_problems = True
    solve_problem_num = 4

    all_problems = problems.init_problems()


    if solve_all_problems:
        for key in all_problems:
            print("\n")
            try:

                problem = all_problems[key]

                if problem.test_solution():
                    print("Test Passed.")
                else:
                    print("Problem number",problem.number,"has either failed the test or has no test input, solution is not reliable.")

                problem.answer = problem.solution(problem.input)
                print("Problem #",problem.number,"\n",problem.description)
                print("The answer to problem ",problem.number," is: ", problem.answer)
            except:
                print("Problem #",problem.number,"\n",problem.description)
                print("This problem has not been solved yet.")
    
    print(all_problems[2].test_solution())


main()   





