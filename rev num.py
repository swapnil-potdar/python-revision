
num = 12345
rev_num = 0
while num > 0:
    rem = num % 10
    rev_num = rem + (rev_num * 10)
    num //=10
print(rev_num)