import sys
t = int(sys.stdin.readline())
s = set()
for _ in range(t):
    command = sys.stdin.readline()
    if "add" in command:
        n = int(command.split()[1])
        if not n in s:
            s.add(n)
        else:
            pass
    elif "remove" in command:
        n = int(command.split()[1])
        if n in s:
            s.remove(n)
        else:
            pass
    elif "check" in command:
        n = int(command.split()[1])
        if n in s:
            print(1)
        else:
            print(0)
    elif "toggle" in command:
        n = int(command.split()[1])
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif "all" in command:
        s = set([i for i in range(1, 21)])
    elif "empty" in command:
        s = set()

    