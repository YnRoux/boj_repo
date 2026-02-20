import sys
import heapq

def solve():
    n, k = map(int, sys.stdin.readline().split())
    
    if n >= k:
        print(n - k)
        return

    MAX = 100001
    dist = [float('inf')] * MAX
    
    dist[n] = 0
    pq = [(0, n)]
    
    while pq:
        d, curr = heapq.heappop(pq)
        
        if dist[curr] < d:
            continue
        
        if curr == k:
            print(d)
            return

        for next_step, weight in [(curr * 2, 0), (curr - 1, 1), (curr + 1, 1)]:
            next_dist = d + weight
            
            if 0 <= next_step < MAX and next_dist < dist[next_step]:
                dist[next_step] = next_dist
                heapq.heappush(pq, (next_dist, next_step))

solve()