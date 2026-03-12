import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    MAX_SIZE = 20001
    deque = [0] * MAX_SIZE
    head = 10000
    tail = 10001

    for _ in range(n):
        command = input().split()
        cmd = command[0]

        if cmd == "push_front":
            deque[head] = command[1]
            head -= 1
        elif cmd == "push_back":
            deque[tail] = command[1]
            tail += 1
        elif cmd == "pop_front":
            if head + 1 == tail:
                print("-1")
            else:
                head += 1
                print(deque[head])
        elif cmd == "pop_back":
            if tail - 1 == head:
                print("-1")
            else:
                tail -= 1
                print(deque[tail])
        elif cmd == "size":
            print(tail - head - 1)
        elif cmd == "empty":
            print(1 if head + 1 == tail else 0)
        elif cmd == "front":
            print(deque[head + 1] if head + 1 != tail else -1)
        elif cmd == "back":
            print(deque[tail - 1] if tail - 1 != head else -1)

solve()