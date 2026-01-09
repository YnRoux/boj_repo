n = int(input())
m = (8 + 7 * (n - 1)) % 12
y = 2024 + (8 + 7 * (n - 1)) // 12
if m == 0:
    m = 12
    y -= 1
print(f"{y} {m}")