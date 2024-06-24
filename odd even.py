num = int(input("Enter a number:"))


def isEven(n):
    return n % 2 == 0
    # return 1 if n%2 == 0 else 0
    # return True if n%2 == 0 else False


if isEven(num):
    print("Even number!")
else:
    print("Odd number!")