# 3 ** p % p = 3
# g * d = 1 mod p

#  tempting to bruteforce .


        pow(a, p) = a mod p
and, if p is prime and a is an integer coprime with p:
        pow(a, p-1) = 1 mod p

        a^(p-1) = 1 (mod p)
        a^(p-1) * a^-1 = a^-1 (mod p)
        a^(p-2) * a * a^-1 = a^-1 (mod p)
        a^(p-2) * 1 = a^-1 (mod p)

        a^(p-2) = a^-1 (mod p)
So, doing a^(p-2) and then (mod p) we can achieve
it
'''

a = 3
p = 13

d = pow(a,p-2) % p
print(d)
