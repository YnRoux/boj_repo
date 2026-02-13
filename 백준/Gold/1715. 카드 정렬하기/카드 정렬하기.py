import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    cost = 0
    while len(cards) > 1:
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)

        sumval = first + second
        cost += sumval

        heapq.heappush(cards, sumval)
    
    print(cost)