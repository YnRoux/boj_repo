import sys

i = 0

while 1:
    data = sys.stdin.readline().rstrip()
    if data == '0':
        break
    i += 1
    r, w, l = map(int, data.split())
    if (2*r)**2 >= w**2 + l**2:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")