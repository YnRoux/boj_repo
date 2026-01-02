import sys
input = sys.stdin.readline
t = int(input().strip())
queue = []
head = 0
for _ in range(t):
    command = input().strip()
    op = command
    if "push" in command:
        op = command.split()[0]

    if op == "push":
        queue.append(int(command.split()[1]))
    elif op == "pop":
        if len(queue) > head:
            print(queue[head])
            head += 1
        else:
            print(-1)
    elif op == "size":
        print(len(queue) - head)
    elif op == "empty":
        if len(queue) == head:
            print(1)
        else:
            print(0)
    elif op == "front":
        if len(queue) > head:
            print(queue[head])
        else:
            print(-1)
    elif op == "back":
        if len(queue) > head:
            print(queue[-1])
        else:
            print(-1)
