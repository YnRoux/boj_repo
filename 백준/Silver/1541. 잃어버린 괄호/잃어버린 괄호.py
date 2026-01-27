expr = input()
sums = [sum(map(int, chunk.split('+'))) for chunk in expr.split('-')]
print(sums[0] - sum(sums[1:]))