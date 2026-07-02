def solution(todo_list, finished):
    l = []
    for i in range(len(todo_list)):
        if not finished[i]:
            l.append(todo_list[i])
    return l