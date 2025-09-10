# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
from math import sqrt
from typing import List


def factors_brute_force(n: int) -> List[int]:
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


print(factors_brute_force(20))

# Better Approach
# Time Complexity: O(n/2)” or “O(n)
# Space Complexity: O(k), where “k” is the number of factors of “num”, as it stores the factors in a list.


def factors(num: int) -> List[int]:
    factors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            factors.append(i)
        factors.append(num)
    return factors


print(factors(20))

# Optimal Approach
# Time Complexity: O(sqrt(n))
# Space Complexity: O(k), where “k” is the number of factors of “num”, as it stores the factors in a list.


def factors(num: int) -> List[int]:
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    factors.sort()
    return factors


print(factors(36))
