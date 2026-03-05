import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    words = [input().rstrip() for _ in range(n)]
    
    word_count = {}
    for word in words:
        if len(word) >= m:
            word_count[word] = word_count.get(word, 0) + 1

    unique_words = list(word_count.keys())
    
    unique_words.sort(key=lambda x: (-word_count[x], -len(x), x))
    
    print('\n'.join(unique_words))

if __name__ == "__main__":
    solve()