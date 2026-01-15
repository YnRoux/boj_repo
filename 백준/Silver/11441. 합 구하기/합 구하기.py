import sys
input = sys.stdin.readline

n = int(input().strip())
num_list = list(map(int, input().strip().split()))

acc_sum = 0
acc_list = [0]
for i in range(n):
    acc_sum += num_list[i]
    acc_list.append(acc_sum)

m = int(input().strip())
for _ in range(m):
    r1, r2 = map(int, input().strip().split())
    r1 -= 1
    print(acc_list[r2] - acc_list[r1])