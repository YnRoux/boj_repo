def solution(myStr):
    myStr = myStr.replace("b", "a").replace("c", "a")
    l = [s for s in myStr.split("a") if s]
    return l if l else ["EMPTY"]