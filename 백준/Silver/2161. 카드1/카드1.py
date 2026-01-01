n = int(input())
queue = list(range(1,n+1))
throw = []
while 1:
    if len(queue) == 1:
        break
    throw.append(queue.pop(0))
    temp = queue.pop(0)
    queue = queue + [temp]
print(*throw, queue[0])