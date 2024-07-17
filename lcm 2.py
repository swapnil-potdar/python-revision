m = m1 = int(input('Primary:'))
n = n1 = int(input("Second:"))
while n:
    m, n = n, m%n
lcm = (m1*n1)//m
print("LCM:", lcm)