year = int(input("Enter year: "))

def leap(year):
  return year%4==0
print("Leap Year" if leap(year) else "Non leap year")