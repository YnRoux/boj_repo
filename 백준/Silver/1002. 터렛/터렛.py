t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d_sq = (x1 - x2)**2 + (y1 - y2)**2

    r_sum_sq = (r1 + r2)**2
    r_diff_abs_sq = (r1 - r2)**2 
    
    if d_sq == 0 and r1 == r2:
        print(-1)
        continue

    if d_sq > r_sum_sq or d_sq < r_diff_abs_sq:
        print(0)
    
    elif d_sq == r_sum_sq or d_sq == r_diff_abs_sq:
        print(1)

    elif r_diff_abs_sq < d_sq < r_sum_sq:
        print(2)