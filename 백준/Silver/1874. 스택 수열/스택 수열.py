import sys
input = sys.stdin.readline

n = int(input())
current = 1
stack, answer = [], []
possible = True

for _ in range(n):
    num = int(input())
    while current <= num:
        stack.append(current)
        answer.append('+')
        current += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(answer))
else:
    print('NO')