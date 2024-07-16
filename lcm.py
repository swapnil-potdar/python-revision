
m = int(input('Primary:'))
n = int(input("Second:"))
large = ref = m if m>n else n
small = n if m>n else m
count = 2
while large % small != 0:
    large = ref
    large *= count
    count +=1
print("LCM", large)