def solve():
    n = int(input())
    m = int(input())
    in_str = input()

    pn = "I" + "OI" * n
    head, tail = 0, 2*n+1
    count = 0

    for i in range(m-2*n):
        head = i
        tail = 2*n + 1 + i
        
        if in_str[head:tail] == pn:
            count += 1

    print(count)

if __name__ == "__main__":
    solve()

