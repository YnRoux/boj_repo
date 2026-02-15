l = []
for _ in range(7):
    name, count = input().split()
    l.append((name, int(count)))
maxlecture = max(l, key=lambda x: x[1])
print(maxlecture[0])