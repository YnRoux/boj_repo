def solution(n):
    l = [[0] * n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, 0
    dir_idx = 0
    for m in range(1, n**2+1):
        l[r][c] = m
        next_r = r + dr[dir_idx]
        next_c = c + dc[dir_idx]
        
        if not (0 <= next_r < n and 0 <= next_c < n) or l[next_r][next_c] != 0:
            dir_idx = (dir_idx + 1) % 4
        r += dr[dir_idx]
        c += dc[dir_idx]
    return l