import sys
h, m, s = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
total_seconds = h * 3600 + m * 60 + s + t
s = total_seconds % 60
m = (total_seconds // 60) % 60
h = (total_seconds // 3600) % 24
print(f"{h} {m} {s}")