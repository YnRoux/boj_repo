import sys
input = sys.stdin.readline

def cut(k, n):
    if n == 1:
        return
    
    for i in range(k + n//3, k + (n//3) * 2):
        res[i] = " "
    
    cut(k, n//3)
    cut(k + (n//3) * 2, n//3)

while 1:
    try:
        n = int(input())
        res = ["-"] * 3 ** n
        cut(0, 3 ** n)
        print("".join(res))
    except:
        break