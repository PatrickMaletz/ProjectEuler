from problemClass import Problem
import MathModule as MM

def init_solutions():
    solutions = []
    solutions.append(solve01)
    solutions.append(solve02)
    solutions.append(solve03)
    solutions.append(solve04)
    solutions.append(solve05)

    return solutions

def solve01(problem_input):
    multiple_sum = 0
    for x in range(problem_input):
        if MM.multiple_of_n(x,3) or MM.multiple_of_n(x,5):
            multiple_sum += x

    return multiple_sum

def solve02(problem_input):
    previous_sum = 1
    next_sum = 0
    sum = 1
    total = 0
    while sum < problem_input:
        if MM.is_even(sum):
            total += sum

        next_sum = MM.next_fibonacci(sum,previous_sum)
        previous_sum = sum
        sum = next_sum

    return total

def solve03(problem_input):
    prime_factor_list = MM.prime_factors(problem_input)

    return max(prime_factor_list)

def solve04(problem_input):
    maximum_number = (10**(problem_input)-1)**2-2
    x = int(maximum_number)
    while x > 0:        
        if MM.is_palindrome(x):            
            x_factors = MM.factorise(x)            
            for factor in x_factors:
                if (len(str(int(factor))) == 3) & (len(str(int(x/factor))) == 3):
                    return x
        x -= 1
    return

def solve05(problem_input):
    x = 1
    while True:
        factors = MM.factorise(x)
        factors.sort()
        for count, factor in enumerate(factors):
            if factor == problem_input:
                
                return x
            elif count+1 == len(factors):
                
                break               
            elif not factors[count+1] == factor+1:
                
                break 

        x += 1
    


            

    return



