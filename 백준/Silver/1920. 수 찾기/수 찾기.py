n = int(input())
a = set(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))
for e in t:
    print(int(e in a))