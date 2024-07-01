number = int(input("Any number:"))
def isPrime(number):
  for i in range(2, (number//2)+1):
    if number%i == 0:
      return False
      break
  return True

if isPrime(number):
  print("{} is a prime number".format(number))
else:
  print("{} is not a prime number".format(number))