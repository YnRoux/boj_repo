expr = input()
chunks = expr.split('-')
res = sum(map(int, chunks[0].split('+')))
for i in range(1, len(chunks)):
    res -= sum(map(int, chunks[i].split('+')))
print(res)