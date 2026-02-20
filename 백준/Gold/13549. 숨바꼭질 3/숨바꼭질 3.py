import sys
from collections import deque

def solve():
    n, k = map(int, sys.stdin.readline().split())
    
    MAX = 100001
    dist = [-1] * MAX
    
    queue = deque([n])
    dist[n] = 0
    
    while queue:
        curr = queue.popleft()
        
        if curr == k:
            print(dist[curr])
            return

        for next_pos in [curr * 2, curr - 1, curr + 1]:
            if 0 <= next_pos < MAX and dist[next_pos] == -1:
                if next_pos == curr * 2:
                    dist[next_pos] = dist[curr]
                    queue.appendleft(next_pos)
                else:
                    dist[next_pos] = dist[curr] + 1
                    queue.append(next_pos)

solve()