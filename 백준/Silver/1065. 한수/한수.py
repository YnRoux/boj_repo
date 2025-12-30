n = int(input())
cnt = 0
for i in range(1, n+1):
    if i < 100:
        cnt += 1
    elif 100 <= i < 1000:
        if (i//100-(i//10)%10) == ((i//10)%10 - (i-(i//10)*10)):
            cnt += 1
print(cnt)