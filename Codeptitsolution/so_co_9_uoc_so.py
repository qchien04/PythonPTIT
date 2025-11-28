import math
def nt(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

def cnt(N):
    primes = nt(int(math.sqrt(N)) + 1)
    count = 0
    for p in primes:
        if p ** 8 <= N:
            count += 1
        else:
            break
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] ** 2 * primes[j] ** 2 <= N:
                count += 1
            else:
                break
    return count

n = int(input())
print(cnt(n))
