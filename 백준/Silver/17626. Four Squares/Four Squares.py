def is_square(n):
    if n < 0:
        return False
    root = int(n**0.5)
    return root**2 == n

def solve():
    n = int(input())

    if is_square(n):
        print(1)
        return
    
    for i in range(1, int(n**0.5) + 1):
        if is_square(n - i**2):
            print(2)
            return
    
    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int((n - i**2)**0.5) + 1):
            if is_square(n - i**2 - j**2):
                print(3)
                return
            
    print(4)

if __name__ == "__main__":
    solve()