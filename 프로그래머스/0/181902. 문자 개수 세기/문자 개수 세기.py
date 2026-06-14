def solution(my_string):
    answer = [0] * 52
    for char in my_string:
        if char.isupper():
            answer[ord(char) - ord('A')] += 1
        elif char.islower():
            answer[ord(char) - ord('a') + 26] += 1
    return answer