def count_p(n, p):
    count = 0
    while n >= p:
        count += n // p
        n //= p
    return count

def solve():
    a = input()
    if not a:
        return
    n, m = map(int, a.split())

    five_count = count_p(n, 5) - count_p(m, 5) - count_p(n - m, 5)
    
    two_count = count_p(n, 2) - count_p(m, 2) - count_p(n - m, 2)

    print(min(five_count, two_count))

solve()