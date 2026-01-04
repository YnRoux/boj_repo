n = int(input())
ss = ''

for i in range(1, n):
    su = '*' * (2*i-1)
    su = su.center(2*n-1, ' ')
    su = su.rstrip()
    ss += su + '\n'

ss += '*' * (2*n-1) + '\n'

for i in range(1, n):
    sl = '*' * (2*n - (2*i+1))
    sl = sl.center(2*n-1, ' ')
    sl = sl.rstrip()
    if not i == n-1:
        ss += sl + '\n'
    else: ss += sl
print(ss)