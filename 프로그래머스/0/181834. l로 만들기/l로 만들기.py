def solution(myString):
    trans_table = str.maketrans("abcdefghijk", "lllllllllll")
    return myString.translate(trans_table)