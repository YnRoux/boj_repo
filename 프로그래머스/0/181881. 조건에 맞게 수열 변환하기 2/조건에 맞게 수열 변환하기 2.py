def solution(arr):
    def trans(r):
        return [
            x // 2 if x >= 50 and x % 2 == 0 
            else (x * 2 + 1) if x < 50 and x % 2 == 1 
            else x 
            for x in r
        ]
    cnt = 0
    while True:
        next_arr = trans(arr)
        if arr == next_arr:
            return cnt
        arr = next_arr
        cnt += 1