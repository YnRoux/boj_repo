def solve():
    n = int(input())
    m = int(input())
    s = input()

    ans = 0  # 최종 P_N 개수
    count = 0  # 연속된 'IOI' 개수
    i = 1  # i-1, i, i+1

    while i < (m-1):
        # 'IOI' 패턴을 찾은 경우
        if s[i-1] == "I" and s[i] == "O" and s[i+1] == "I":
            count += 1
            # 연속된 IOI가 N개 쌓이면 P_N을 찾은 것
            if count == n:
                ans += 1
                # 다음 IOI가 나왔을 때 중첩된 부분을 계산하기 위해 1을 빼줌
                count -= 1
            i += 2  # IOI를 확인했으므로 다음 패턴 확인을 위해 2칸 이동
        else:
            # 패턴이 끊기면 연속 횟수 초기화
            count = 0
            i += 1

    print(ans)

if __name__ == "__main__":
    solve()

