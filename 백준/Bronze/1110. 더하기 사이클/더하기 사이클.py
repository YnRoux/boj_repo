n = int(input())
i = 0
m = n
while 1:
    if i != 0 and m == n:
        break
    i += 1
    a, b = m // 10, m % 10
    c = (a + b) % 10
    a, b = b, c
    m = 10*a + b
print(i)