def mergesort(l):
    if len(l) == 1:
        return l
    
    mid = (len(l)+1) // 2
    left = mergesort(l[:mid])
    right = mergesort(l[mid:])

    li = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            li.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            li.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left):
        li.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        li.append(right[j])
        ans.append(right[j])
        j += 1
    
    return li

a, k = map(int, input().split())
l = list(map(int, input().split()))

ans = []
mergesort(l)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)