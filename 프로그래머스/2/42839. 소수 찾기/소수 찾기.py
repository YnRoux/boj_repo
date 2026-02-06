from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
            
    return True

def solution(numbers):
    candidate_set = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        
        for p in perms:
            num = int("".join(p))
            candidate_set.add(num)
    
    prime_count = 0
    for num in candidate_set:
        if is_prime(num):
            prime_count += 1
            
    return prime_count