# 2346

from collections import deque

n = int(input())
deq = deque(enumerate(map(int, input().split())))
res = []
 
while deq:
    idx, now_turn = deq.popleft()
    res.append(idx + 1)
 
    if now_turn > 0:
        deq.rotate(-(now_turn - 1))
    elif now_turn < 0:
        deq.rotate(-now_turn)
 
print(' '.join(map(str, res)))