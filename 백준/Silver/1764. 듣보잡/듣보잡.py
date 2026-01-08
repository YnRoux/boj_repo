import sys
input = sys.stdin.readline
n, m = map(int, input().split())

s1 = {input().strip() for _ in range(n)} 
s2 = {input().strip() for _ in range(m)}

l = sorted(list(s1 & s2))
print(len(l))
print('\n'.join(l))