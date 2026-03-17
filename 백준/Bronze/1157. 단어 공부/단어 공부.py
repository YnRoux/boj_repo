s = input().upper()
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
idx = []
for A in ABC:
    idx.append(s.count(A))
allidx = list(filter(lambda x : idx[x] == max(idx), range(len(idx))))
if len(allidx) == 1:
    print(f'{ABC[allidx[0]]}')
else: print('?')