# CORRECT SPECIFICATION:
#
# isPrime checks if a positive integer is prime.
#
# A positive integer is prime if it is greater than 
# 1, and its only divisors are 1 and itself.
#
# TASKS:
#
# 1) Add an assertion to test() that shows
#    isPrime(number) to be incorrect for 
#    some input.
#
# 2) Write isPrime2(number) to correctly 
#    check if a positive integer is prime.

import math

def isPrime(number):
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))):  
        if (number%check) == 0:  
            return False
    return True

def isPrime2(number):  
    ###Your isPrime2 code here.

    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.ceil(math.sqrt(number))) + 1):  
        if (number%check) == 0:  
            return False
    return True

def test():
    primes = [2, 3, 5, 11, 13, 23] 
    nonprimes = [1, 4, 20, 21, 22, 24, 25, 49] 
    
    for val in primes: 
        test_val(val, True)

    for val in nonprimes: 
        test_val(val, False)


def test_val(val, expected): 
    result = isPrime2(val)
    assert(result == expected)

if __name__ == "__main__":
    test() 