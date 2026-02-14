data = input()
res = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    res += str(data.count(letter)) + " "
print(res.rstrip())