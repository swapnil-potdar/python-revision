upto = int(input('Fabinacci sequence upto: '))

print("Fabinacci sequence:", end= " ")
n = 0
m = 1
if upto ==0:
  print(n)
elif upto == 1:
  print(n,m)
else:
  print(n, m, end=' ')
  for i in range(2, upto+1):
    o = m
    m = m + n
    n = o
    print(m, end = ' ')

