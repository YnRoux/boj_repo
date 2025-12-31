n = int(input())
power = 1

while 1:
    if (n == 1 or n == 2):
        print(n)
        break
    power += 1
    if (2**power >= n):
        print((n-2**(power-1))*2)
        break