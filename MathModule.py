

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

def prime_factors(num):
    #Prime number factorisation
    #Recursive
    if is_prime(num):
        return num
    factors = factorise(num)
    factors.sort()
    factors = [factors[0],int(num/factors[0])]
    prime_factor_list = []
    for factor in factors:
        if is_prime(factor):
            prime_factor_list.append(factor)
        else:
            prime_factor_list += prime_factors(factor)


    return prime_factor_list

