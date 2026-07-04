def solution(myString, pat):
    s = ""
    for e in myString:
        if e == "A":
            s += "B"
        else:
            s += "A"
    return int(pat in s)