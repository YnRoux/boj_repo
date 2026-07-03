def solution(myString):
    myString =  myString.lower()
    for i in range(len(myString)):
        if myString[i] == "a":
            myString = myString[:i] + "A" + myString[i+1:]
    return myString