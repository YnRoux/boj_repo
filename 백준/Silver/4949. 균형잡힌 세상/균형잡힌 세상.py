while 1:
    in_str = input()
    if in_str == ".":
        break
    stack = []

    for e in in_str:
        if e == "[" or e == "(":
            stack.append(e)
        elif e == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif e == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
    if not stack:
        print("yes")
    else:
        print("no")