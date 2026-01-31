l = [int(input()) for _ in range(5)]
l = list(map(lambda x: 40 if x < 40 else x, l))
print(sum(l)//5)