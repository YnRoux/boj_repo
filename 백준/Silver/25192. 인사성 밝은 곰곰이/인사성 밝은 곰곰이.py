import sys
input = sys.stdin.readline

n = int(input().rstrip())

bear_emoji = set()
s = 0

for _ in range(n):
    in_str = input().rstrip()
    if in_str == "ENTER":
        s += len(bear_emoji)
        bear_emoji = set()
    else:
        bear_emoji.add(in_str)

s += len(bear_emoji)

print(s)