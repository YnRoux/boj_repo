t = int(input())
l = [input() for _ in range(t)]
res = []

for col in zip(*l):
    if len(set(col)) == 1:
        res.append(col[0])
    else:
        res.append("?")

print("".join(res))