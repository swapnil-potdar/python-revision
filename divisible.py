number = int(input("Enter number: "))
upto = int(input('enter a number upto we have to check: '))
divisible = list(filter(lambda y: y%number ==0, list(range(1,upto+1))))
print(f"The list of numbers which are divisible by {number} are {divisible}")