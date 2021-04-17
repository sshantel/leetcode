"""
Count the number of prime numbers less than a non-negative number, n.

"""
def countPrimes(n):
    primes = [] 
    print(type(n))
    print(int(n))
    for i in range(2,((n)/2)):
        if i % 2 != 0:
            primes.append(i)
    return len(primes)