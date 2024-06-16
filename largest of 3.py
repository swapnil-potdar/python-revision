
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a>b and a>c:
  print(f"{a} is a largest number.")
elif b>c:
  print(f"{b} is a largest number.")
else:
  print(f"{c} is a largest number.")