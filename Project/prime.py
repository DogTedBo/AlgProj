import random
import math

def sieve_of_eratosthenes(max_number):
    """Generate all prime numbers up to max_number."""
    is_prime = [True] * (max_number + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    primes = []

    for number in range(2, int(max_number ** 0.5) + 1):
        if is_prime[number]:
            primes.append(number)
            # Mark multiples of number as non-prime
            for multiple in range(number*number, max_number + 1, number):
                is_prime[multiple] = False

    # Adding remaining prime numbers to the list
    for number in range(int(max_number ** 0.5) + 1, max_number + 1):
        if is_prime[number]:
            primes.append(number)

    return primes

def rabin_miller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def is_prime(num):
    if num < 2:
        return False
    
    small_primes = sieve_of_eratosthenes(997)
    if num in small_primes:
        return True

    for prime in small_primes:
        if num % prime == 0:
            return False

    return rabin_miller(num)


def get_prime(key_size=1024):
    while True:
        num = random.randrange(2**(key_size-1), 2**key_size)
        if is_prime(num):
            return num


p=get_prime(15)
q=get_prime(15)

print('q',q)
print('p',p)

n=p*q
phi=(p-1)*(q-1)

print('n',n)
print('phi',phi)

e = random.randint(2, phi)
while math.gcd(e, phi) != 1: 
    e = random.randint(2, phi) 
print('e',e)
       
def extended_gcd(a =1, b = 1): 
    if b == 0: 
        return (1, 0, a)  
    (x, y, d) = extended_gcd(b, a%b)  
    return y, x - a//b*y, d
       
x = extended_gcd(e, phi)
d = x[0] % phi
print('d',d)

message='topSecret'            #------------------------according to the input ifo
message = message.upper()

for M in message:  
    M = ord(M)
    
    print(M)
    C=pow(M,e,n)
    M=pow(C,d,n)
    print(C)
    print(M)

S=pow(M,d,n)
print(S)
m=pow(S,e,n)
print(m)

