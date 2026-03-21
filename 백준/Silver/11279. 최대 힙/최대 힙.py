import sys
import heapq

input = sys.stdin.read
data = input().split()
n = int(data[0])
heap = []
results = []

for i in range(1, n + 1):
    x = int(data[i])
    if x == 0:
        if not heap:
            results.append("0")
        else:
            results.append(str(-heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -x)

print("\n".join(results))