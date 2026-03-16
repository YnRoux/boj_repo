def cnt(n, k):
    if n <= 0:
        return 0
    if k == 2:
        return max(0, n-2)
    elif k == 3:
        if n < 6:
            return 0
        else:
            return (n//3) -1
    elif k == 4:
        if n < 10:
            return 0
        res = (n//2) - 4
        if n >= 12:
            res -= 1
        return max(0, res)
    elif k == 5:
        if n < 15:
            return 0
        return (n//5) - 2
    

l = int(input())
r = int(input())
k = int(input())

print(cnt(r, k) - cnt(l-1, k))