import utilityModule


def multiple_of_n(input_num,n):
    
    if input_num%n == 0:
        return True
    else:
        return False

def next_fibonacci(num, previous_num):
    return num+previous_num

def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False

def factorise(num: int):
    #Returns a list of factors for a given input integer
    x = 2
    factors = []
    while x <= num**0.5:
        if num%x == 0:
            factors.append(int (x))
            if x != num/x:
                factors.append(int (num/x))
        x+= 1
    
    return factors

def is_prime(num):
    #Returns True if an inpout number is prime
    factors = factorise(num)
    
    if not (len(factors) == 0) or num == 1:
        return False
    else:
        return True

def prime_factors(num):
    #Returns a list of all the prime factors of a given number
    factors = factorise(num)
    prime_list = []
    for factor in factors:
        if is_prime(factor):
            prime_list.append(factor)
    
    return prime_list

def is_palindrome(num):
    #Checks if number is palindrome (reads same back to front)
    num_str = str(num)
    start = 0
    end = len(num_str)

    while start < len(num_str)/2:
        if not (num_str[start] == num_str[end-1]):
            return False
        else:
            start += 1
            end -= 1
            
    return True

def prime_factor_decomposition(num):
    #Prime number factorisation
    #Recursive
    if is_prime(num):
        return [num]
    factors = factorise(num)
    factors.sort()
    factors = [factors[0],factors[-1]]
    prime_factor_list = []
    for factor in factors:
        if is_prime(factor):
            prime_factor_list.append(factor)
        else:
            prime_factor_list += prime_factor_decomposition(factor)


    return prime_factor_list

def in_list(item,list):
    #Returns a list of the positions where item is list
    positions = []
    for count,list_item in enumerate(list):
        if item == list_item:
            positions.append(count)
    return positions

def multiplyList(myList):
    #Returns the product of all elements in a list
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

def calc_square_sum(num_list):
    #Returns the sum of all the numbers in a list squared.
    square_sum = 0
    for num in num_list:
        square_sum += num**2
    return square_sum

def calc_sum_square(num_list):
    #Returns the square of the sum of a list of numbers
    return sum(num_list)**2

def list_prime_numbers(n, use_number = True):
    #Lists prime numbers
    #If use_number = True -> returns the first n prime numbers.
    #If use_number = False -> returns all the prime numbers below
    prime_list = []
    num = 1
    if use_number:
        while len(prime_list )< n:
            if is_prime(num):
                prime_list.append(num)

            num += 1
    else:
        while num < n:
            if is_prime(num):
                prime_list.append(num)

            num += 1
    
    return prime_list

def prime_sieve(n):
    #Lists all the prime numbers up to n
    # Uses Sieve of Eratosthenes
    prime_list = []
    prime_bools = [True]*(n)
    i = 2
    while i < n**0.5:
        if prime_bools[i]:
            j = i**2
            while j < (n):
                prime_bools[j] = False
                j += i
        i += 1
    k = 0
    for prime_bool in prime_bools:
        if prime_bool:
            prime_list.append(k)
        k += 1
                    

    return prime_list

def sum_of_list(number_list):
    sum = 0
    for num in number_list:
        sum += int(num)
    
    return sum

def product_of_list(number_list):
    sum = 1
    for num in number_list:
        sum = sum*int(num)
    
    return sum

def make_pythag_triplet(m,n):
    #Returns a pythagorean triplet using Euclid's formula.
    if n > m:
        return
    
    a = m**2-n**2
    b = 2*m*n
    c = m**2+n**2

    return a,b,c

def scan_array(array, scan_size, direction, start_point):
    #Returns a list of numbers that are in a linear scan of a 2D grid array given a scan length, direction and starting point.
    count = 0
    scan = []
    while count < scan_size:
        row = start_point[0]+count*direction[0]
        column = start_point[1]+count*direction[1]
        
        scan.append(array[row][column])

        count += 1
    
    return scan

def next_collatz_number(number: int) -> int:
    
    if is_even(number):
        return int(number/2)

    else:
       return int(number*3+1)

def collatz_sequence(number: int):
    next_number = number
    collatz_numbers: list(int) = [number]

    while next_number != 1:
         next_number = next_collatz_number(next_number)
         collatz_numbers.append(next_number)

    return collatz_numbers


def goto_grid_corner(n, node, count):
    #print(node.data)
    #Find the corner of a grid using a binary tree
    if node.data[0] == n or node.data[1] == n:

        #print(node.data, "Woppedywoop")
        count += 1
        return count


    left_node = utilityModule.node(data = [node.data[0]+1,node.data[1]])
    node.left = left_node 

   
    right_node = utilityModule.node(data = [node.data[0],node.data[1]+1])
    node.right = right_node
    
    count = goto_grid_corner(n,node.left, count)
    count = goto_grid_corner(n,node.right, count)

       
    return count
        
