hcf1 = int(input('HCf_1:'))
hcf2 = int(input('HCF_2:'))

def gcd(hcf1, hcf2):
    small = hcf1 if hcf2 > hcf1 else hcf2
    for i in range(small+1,1,-1):
        if ((hcf1 % i == 0) and (hcf2 % i == 0)):
            return i

print(gcd(hcf1, hcf2))