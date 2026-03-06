import sys
input = sys.stdin.readline

def recursion(s, l, r, i):
    i += 1
    if l >= r:
        print(1, i)
    elif s[l] != s[r]:
        print(0, i)
    else:
        return recursion(s, l+1, r-1, i)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

n = int(input())
for _ in range(n):
    isPalindrome(input().rstrip())