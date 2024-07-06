start = int(input("Enter first number: "))
stop = int(input('Enter final number:'))

def isArmstrong(n):
  str_n = str(n)
  count = len(str_n)
  armstrong = 0
  for j in str_n:
    armstrong += int(j)**count
  if armstrong == n:
    return n
for i in range(start, stop+1):
  if isArmstrong(i):
    print(i, end = " ")