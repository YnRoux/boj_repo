for i in range(3, 0, -1):
    a = input()
    if a not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(a) + i
print("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n)