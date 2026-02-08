import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    meeting = set()
    for _ in range(n):
        ai, bi = input().rstrip().split()
        if ai == "ChongChong" or bi == "ChongChong":
            meeting.add(ai)
            meeting.add(bi)
        elif (ai in meeting) or (bi in meeting):
            meeting.add(ai)
            meeting.add(bi)
    print(len(meeting))

if __name__ == "__main__":
    solve()