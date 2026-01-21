import sys

n = int(input())

end_pos = 0
res = 0

arr = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr.append([a, b])

arr.sort(key=lambda x: (x[1], x[0]))

for new_ini, new_end in arr:
    if end_pos <= new_ini:
        res += 1
        end_pos = new_end
print(res)