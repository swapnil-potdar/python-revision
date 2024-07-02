start = int(input("Enter start:"))
stop = int(input("Enter stop:"))

def isPrime(n):
  for j in range(2, (n//2)+1):
    if i%j == 0:
      return False
  return True

for i in range(start, stop+1):
  if isPrime(i):
    print(i, end=" ")