import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    commend = input().strip()
    if " " in commend:
        commend, num_in = commend.split()[0], int(commend.split()[1])
    if commend == "1":
        stack.append(num_in)
    elif commend == "2":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif commend == "3":
        print(len(stack))
    elif commend == "4":
        if stack:
            print(0)
        else:
            print(1)
    elif commend == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)