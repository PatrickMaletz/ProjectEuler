from problemClass import Problem
import MathModule as MM
import solutions
import problems

def main():
    solved_problems = 3
    Problems = []
    
    Problem01 = problems.problem01()
    Problem01.answer = solutions.solve01(Problem01.input)
    

    Problem02 = problems.problem02()
    Problem02.answer = solutions.solve02(Problem02.input)

    Problem03 = problems.problem03()
    Problem03.answer = solutions.solve03(Problem03.input)
    print(Problem03.answer)
    print(MM.is_prime(Problem03.answer))
main()   





