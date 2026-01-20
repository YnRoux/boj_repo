import sys
input = sys.stdin.readline

def num_sum(serial_number):
    s = 0
    for char in serial_number:
        try:
            s += int(char)
        except:
            pass
    return s

n = int(input().strip())
l = [input().strip() for _ in range(n)]
l.sort(key=lambda x: (len(x), num_sum(x), x))

for element in l:
    print(element)
