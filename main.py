from problemClass import Problem
import MathModule as MM
import solutions
import problems

def main():
    Problem01 = problems.problem01()
    Problem01.answer = solutions.solve01(Problem01.input)

    Problem02 = problems.problem02()
    Problem02.answer = solutions.solve02(Problem02.input)

    print(Problem02.answer)
main()   





