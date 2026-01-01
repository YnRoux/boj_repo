import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    commend = input().strip()
    if " " in commend:
        commend, num_in = commend.split()[0], int(commend.split()[1])
    if commend == "push":
        stack.append(num_in)
    elif commend == "pop":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif commend == "size":
        print(len(stack))
    elif commend == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif commend == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)