n, k = map(int, input().split())
arr = list(range(1, n + 1))
result = []
index = 0

for _ in range(n):
    index = (index + k - 1) % len(arr)
    result.append(arr.pop(index))

print(f"<{', '.join(map(str, result))}>")