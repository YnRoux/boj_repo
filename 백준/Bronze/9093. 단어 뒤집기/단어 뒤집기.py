t = int(input())
for _ in range(t):
    l = input().split()
    m = [e[::-1] for e in l]
    print(" ".join(m))