def extend_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extend_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)

q = 32321
p = 26513


gcd, u, v = extend_gcd(p, q)
print("[+] GCD: {}".format(gcd))
print("[+] u,v: {},{}".format(u,v))
print("\n[*] FLAG: crypto{{{},{}}}".format(u,v))