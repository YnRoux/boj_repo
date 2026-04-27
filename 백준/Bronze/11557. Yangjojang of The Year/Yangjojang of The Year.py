import sys

def solve():
    input_data = sys.stdin.read().split()    
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        best_school = ""
        max_alcohol = -1
        for _ in range(n):
            school = input_data[idx]
            alcohol = int(input_data[idx+1])
            idx += 2
            if alcohol > max_alcohol:
                max_alcohol = alcohol
                best_school = school
        print(best_school)
solve()