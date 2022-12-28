import MathModule as MM
import utilityModule
def init_solutions():

    solutions = {1:solve01,
    2:solve02,
    3:solve03,
    4:solve04,
    5:solve05,
    6:solve06,
    7:solve07,
    8:solve08,
    9:solve09,
    10:solve10,
    11:solve11,
    12:solve12,
    13:solve13,
    14:solve14,
    15:solve15}

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
            print(sum)
            total += sum

        next_sum = MM.next_fibonacci(sum,previous_sum)
        previous_sum = sum
        sum = next_sum

    return total

def solve03(problem_input):
    prime_factor_list = MM.prime_factors(problem_input)

    return max(prime_factor_list)

def solve04(problem_input):
    maximum_number = (10**(problem_input)-1)**2
    x = int(maximum_number)
    while x > 0:        
        if MM.is_palindrome(x):       
            x_factors = MM.factorise(x)            
            for factor in x_factors:
                if (len(str(int(factor))) == problem_input) & (len(str(int(x/factor))) == problem_input):
                    return x
        x -= 1
    return

def solve05(problem_input):
    """
    The number that contains the all the numbers that are less than the input
    must include every prime factor for each of the other numbers.
    """
    factor_list = []
    for x in range(2,problem_input+1):
        prime_factors = MM.prime_factor_decomposition(x)
        for prime_factor in prime_factors:
            
            quantity = prime_factors.count(prime_factor)
            quantity_in_ist = len( MM.in_list(prime_factor,factor_list))
            if  quantity_in_ist< quantity:
                missing_factors = [prime_factor]*(quantity-quantity_in_ist)
                factor_list += missing_factors
                           

    return MM.multiplyList(factor_list)

def solve06(problem_input):
    numbers = range(1,problem_input+1)
    return MM.calc_sum_square(numbers)-MM.calc_square_sum(numbers)

def solve07(problem_input):
    
    return MM.list_prime_numbers(problem_input)[-1]

def solve08(problem_input):
    value = 0
    giant_number = "73167176531330624919225119674426574742355349194934"
    giant_number += "96983520312774506326239578318016984801869478851843"
    giant_number +=  "85861560789112949495459501737958331952853208805511"
    giant_number +=  "12540698747158523863050715693290963295227443043557"
    giant_number +=  "66896648950445244523161731856403098711121722383113"
    giant_number +=  "62229893423380308135336276614282806444486645238749"
    giant_number +=  "30358907296290491560440772390713810515859307960866"
    giant_number +=  "70172427121883998797908792274921901699720888093776"
    giant_number +=  "65727333001053367881220235421809751254540594752243"
    giant_number +=  "52584907711670556013604839586446706324415722155397"
    giant_number +=  "53697817977846174064955149290862569321978468622482"
    giant_number +=  "83972241375657056057490261407972968652414535100474"
    giant_number +=  "82166370484403199890008895243450658541227588666881"
    giant_number +=  "16427171479924442928230863465674813919123162824586"
    giant_number +=  "17866458359124566529476545682848912883142607690042"
    giant_number +=  "24219022671055626321111109370544217506941658960408"
    giant_number +=  "07198403850962455444362981230987879927244284909188"
    giant_number +=  "84580156166097919133875499200524063689912560717606"
    giant_number +=  "05886116467109405077541002256983155200055935729725"
    giant_number +=  "71636269561882670428252483600823257530420752963450"

    n = problem_input
    greatest_sum = 0
    while n <len(giant_number):
        sum = MM.product_of_list(giant_number[n-problem_input:n])
        if sum > greatest_sum:
            greatest_sum = sum

        n += 1 
    
    return greatest_sum



def solve09(problem_input):
    #Uses Euclid's formula for generating pythagorean triplets.
    m = 2
    
    while m < problem_input:

        n = (problem_input-(2*m**2))/(2*m)
        if (m > n) and n.is_integer() and n > 0:
            triplet = MM.make_pythag_triplet(m,n)
            return MM.product_of_list(triplet)
        m+= 1

    return None

def solve10(problem_input):
    
    return sum(MM.prime_sieve(problem_input)-1)

def solve11(problem_input):
    scan_size = 4
    grid = problem_input
    biggest_scan_product = 0
    scans = []
    scan_up, scan_down, scan_left, scan_right = False, False, False, False
    directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]] #[Up, down, left, right, up-left, up-right, down-left, down-right]
    for row in range(len(grid)):
        scan_up = row+1 >= scan_size
        scan_down =  row <= (len(grid)-scan_size)
        for column in range(len(grid[row])):

            scan_left = column+1 >= scan_size
            scan_right = column <= (len(grid[row])-scan_size)
            direction_bools = [scan_up, scan_down, scan_left, scan_right, scan_up and scan_left, scan_up and scan_right, scan_down and scan_left, scan_down and scan_right]

            for direction, direction_bool in zip(directions,direction_bools):
               
                if direction_bool:
                    scan_product = MM.product_of_list(MM.scan_array(grid,scan_size,direction,[row,column])) 
                    scans.append(scan_product)
            
    biggest_scan_product = max(scans)    
    return biggest_scan_product


def solve12(problem_input):
    factors = 0
    count = 1
    triangle_number = 0
    while factors < problem_input:
        triangle_number +=count
        count += 1
        factors = len(MM.factorise(triangle_number))+2
        print(triangle_number, " ", factors)

        

    return triangle_number

def solve13(problem_input):

    num_sum = 0
    numbers = utilityModule.csv_to_matrix('problem_data/problem_13.csv',' ')
    additional_accuracy = len(str(len(numbers)*10))
    for count in range(len(numbers)):
        num_string = str(numbers[count][0])[0:problem_input+additional_accuracy]
        num_sum += int(num_string)
        
    return str(num_sum)[:problem_input]

def solve14(problem_input): 
    max_num: int = 0
    max_size: int = 0
    for count in range(1,problem_input):
        
        collatz_length = len(MM.collatz_sequence(count))-1
        if collatz_length > max_size:
            max_size = collatz_length
            max_num = count

    return max_num

"""
def solve15(problem_input): 
    start = [0,0]
    root = utilityModule.node(data = start)



    return MM.goto_grid_corner(problem_input,root,0)

"""

def solve15(problem_input):
    n = (problem_input*2)
    count = int(2**(n/2)-1)
    end = 2**n-1
    routes = 0
    i = 2**10-1
    b = bin(i)
    s = str(b)
    s2 = s[2:]
    print(count)
    print(end)
    while(count<end):

        binary_num = str(bin(count))[2:]
        if MM.sum_of_list(binary_num) == n/2:
            routes += 1
        count +=1

    return routes