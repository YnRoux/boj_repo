i = 0
while 1:
    in_data = input()
    if in_data == "0 0 0":
        break
    i += 1
    l = list(map(int, in_data.split()))
    idx = l.index(-1)
    if l[2] == -1:
        c = (l[0] ** 2 + l[1] ** 2) ** (1/2)
        print(f"Triangle #{i}\nc = {c:.3f}")
    else:
        if (l[2] <= l[0]) or (l[2] <= l[1]):
            print(f"Triangle #{i}\nImpossible.")
        else:
            if idx == 0:
                side = "a" 
            else:
                side = "b"
            oth_idx = 1 - idx
            length = (l[2] ** 2 - l[oth_idx] ** 2) ** (1/2)
            print(f"Triangle #{i}\n{side} = {length:.3f}")
    print()