def solution(arr, delete_list):
    for i in delete_list:
        while i in arr:
            del arr[arr.index(i)]
    return arr