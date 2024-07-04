
number = int(input())
copy = number
armstrong = 0
count = len(str(number))

while number >0:
  remainder = number % 10
  armstrong += remainder**count
  number //= 10

if armstrong == copy:
  print(f"{copy} is an Armstrong number.")
else:
  print("not an armstrong number")