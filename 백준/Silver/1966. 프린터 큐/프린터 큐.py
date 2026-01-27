import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    queue = deque([(val, idx) for idx, val in enumerate(imp)])
    
    cnt = 0

    while 1:
        front = queue.popleft()
        if any(front[0] < x[0] for x in queue):
            queue.append(front)
        else:
            cnt += 1
            if front[1] == M:
                print(cnt)
                break