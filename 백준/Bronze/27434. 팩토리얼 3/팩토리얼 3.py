i = int(input())
if i == 0: print(1)
else:
    b = 1
    for a in range(1,i+1):
        b *= a
    print(b)