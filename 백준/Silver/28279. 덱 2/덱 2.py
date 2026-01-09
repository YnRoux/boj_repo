import sys
input = sys.stdin.readline

n = int(input().strip())

deque_dict = {}
head = 0
tail = -1

for _ in range(n):
    command = input().split()
    cmd_type = command[0]
    
    if cmd_type == "1":
        head -= 1
        deque_dict[head] = int(command[1])
        
    elif cmd_type == "2":
        tail += 1
        deque_dict[tail] = int(command[1])
        
    elif cmd_type == "3":
        if head > tail:
            print(-1)
        else:
            print(deque_dict[head])
            head += 1
            
    elif cmd_type == "4":
        if head > tail:
            print(-1)
        else:
            print(deque_dict[tail])
            tail -= 1
            
    elif cmd_type == "5":
        print(tail - head + 1)
    
    elif cmd_type == "6":
        if head > tail:
            print(1)
        else:
            print(0)
            
    elif cmd_type == "7":
        if head > tail:
            print(-1)
        else:
            print(deque_dict[head])
            
    elif cmd_type == "8":
        if head > tail:
            print(-1)
        else:
            print(deque_dict[tail])