

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
    x = 1
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
    
    if len(factors) == 2:
        return True
    else:
        return False

def prime_factors(num):
    #Returns a list of all the prime factors of a given number
    factors = factorise(num)
    prime_list = []
    for factor in factors:
        if is_prime(factor):
            prime_list.append(factor)
    
    return prime_list

