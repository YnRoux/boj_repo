s, p = map(int, input().split())
dna = input()
min_cnt = list(map(int, input().split()))
dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(p):
    dic[dna[i]] += 1

ans = 0

def check():
    if dic['A'] >= min_cnt[0] and dic['C'] >= min_cnt[1] and \
       dic['G'] >= min_cnt[2] and dic['T'] >= min_cnt[3]:
        return True
    return False

if check():
    ans += 1

for i in range(p, s):
    dic[dna[i-p]] -= 1
    dic[dna[i]] += 1

    if check():
        ans += 1

print(ans)