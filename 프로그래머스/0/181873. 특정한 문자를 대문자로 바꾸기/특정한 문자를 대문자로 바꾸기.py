def solution(my_string, alp):
    for i in range(len(my_string)):
        if my_string[i] == alp:
            my_string = my_string[:i] + alp.upper() + my_string[i+1:]
    return my_string