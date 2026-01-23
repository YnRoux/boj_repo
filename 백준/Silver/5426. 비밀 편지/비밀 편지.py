import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    in_str = input().rstrip()
    sq = int((len(in_str))**(1/2))
    str_mat = [[in_str[sq*i+j] for j in range(sq)] for i in range(sq)]
    trans_str = list(zip(*str_mat))
    trans_str = trans_str[::-1]
    for i in range(sq):
        for j in range(sq):
            print(trans_str[i][j], end="")
    print()