def solution(number):
    return sum(map(int,list(str(number)))) % 9