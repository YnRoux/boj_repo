import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    arr.sort()

    cnt = 1
    max_val = arr[0][1]
    for i in range(1, n):
        if max_val > arr[i][1]:
            cnt += 1
            max_val = arr[i][1]
    print(cnt)