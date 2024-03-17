# def sieve(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = False
#     return [i for i in range(n + 1) if primes[i]]

# def max_prime_sum(n):
#     primes = sieve(n)
#     dp = [0] + [0]*n
#     for i in range(1, n+1):
#         for prime in primes:
#             if prime > i:
#                 break
#             dp[i] = max(dp[i], dp[i-prime]+1)
#     return dp[n]

# def sieve(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = False
#     return [i for i in range(n + 1) if primes[i]]

import array

def sieve(n):
    primes = array.array('b', [1] * (n + 1))
    primes[0] = primes[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]


def max_prime_sum(n):
    primes = sieve(n)
    dp_i, dp_i_2, dp_i_1 = 0, 0, 0
    for i in range(1, n+1):
        for prime in primes:
            if prime > i:
                break
            if i >= prime:
                dp_i = max(dp_i_1, dp_i_2 + 1)
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i


n = int(input())
print(max_prime_sum(n))











