import problems

def main():
    solve_all_problems = True
    solve_problem_num = 4

    all_problems = problems.init_problems()


    if solve_all_problems:
        for key in all_problems:
            try:
                problem = all_problems[key]
                problem.answer = problem.solution(problem.input)
                print("Problem #",problem.number,"\n",problem.description)
                print("The answer to problem ",problem.number," is: ", problem.answer)
            except:
                print("Problem #",problem.number,"\n",problem.description)
                print("This problem has not been solved yet.")
                
main()   





