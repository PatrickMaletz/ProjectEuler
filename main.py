import problems
import solutions
import MathModule as MM
import utilityModule as UM
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
    
    current_problem_number = 13
    current_problem = all_problems[current_problem_number] 
    print(current_problem.solution(10))
    #array = [[1,2,3],[4,5,6],[7,8,9]]
    #print(MM.scan_array(array,2,[0,1],[1,0]))
    
    #print((MM.list_prime_numbers_sieve(30)))

   
    #print(UM.csv_to_matrix('problem_data/problem_11.csv',' ')[2][4])

main()   





