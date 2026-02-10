from bisect import bisect_left

def solve():
    n = int(input())
    l = list(map(int, input().split()))
    seq = [l[0]]
    
    for i in range(1, n):
        if l[i] > seq[-1]:
            seq.append(l[i])
        else:
            idx = bisect_left(seq, l[i])
            seq[idx] = l[i]
    
    print(len(seq))

if __name__ == "__main__":
    solve()