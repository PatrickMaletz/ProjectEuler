import problems
import solutions
def main():
    solve_all_problems = False
    solve_problem_num = 4
    print_description = False

    all_problems = problems.init_problems()


    if solve_all_problems:
        for key in all_problems:
            print("\n")
            try:

                problem = all_problems[key]

                problem.test_solution()


                problem.answer = problem.solution(problem.input)
                if print_description : print("Problem #",problem.number,"\n",problem.description) 
                print("The answer to problem ",problem.number," is: ", problem.answer)
            except:
                print("Problem #",problem.number,"\n",problem.description)
                print("This problem has not been solved yet.")
    

main()   





