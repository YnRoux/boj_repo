n = int(input())
a = 1
b = n

while 1:
    c = (a + b) // 2
    if c ** 2 == n:
        print(c)
        break
    elif c ** 2 > n:
        b = c
    elif c ** 2 < n:
        a = c