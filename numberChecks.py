def get_primes(limit):
    """Gets a list of all primes below limit"""
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

def is_prime(num):
    """Checks if a number is prime or not"""
    return num in get_primes(num)
