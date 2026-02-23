def solve():
    n = int(input())
    nodes = list(map(int, input().split()))
    target = int(input())

    tree = [[] for _ in range(n)]
    root = -1

    for i in range(n):
        if nodes[i] == -1:
            root = i
        else:
            if i != target:
                tree[nodes[i]].append(i)
    
    if root == target:
        print(0)
        return
    leaf_count = 0
    stack = [root]

    while stack:
        curr = stack.pop()
        children = tree[curr]
        if not children:
            leaf_count += 1
        else:
            for child in children:
                stack.append(child)
                
    print(leaf_count)


if __name__ == "__main__":
    solve()