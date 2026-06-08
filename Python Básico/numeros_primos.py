""" numeros primos"""

def some_divisor(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    
    return False

def is_prime(n):
    if n <= 1:
        return False
    return not some_divisor(n)

def filter_primes(list_1):
    new_list = []
    
    for number in list_1:
        if is_prime(number):
            new_list.append(number)
    
    return new_list


print(filter_primes([1,2,3,4,5,6,7,8,9,10]))