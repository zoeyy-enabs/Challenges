def scalar_mult(p, n, ec = EllipticCurve(497, 1768, 9739)):
    q = deepcopy(p)
    r = Point()
    while n > 0:
        if n % 2 == 1:
            r = r + q
        q = q + q
        n //= 2
    return r
 def __mul__(self, n):
        return scalar_mult(self, n)
p = Point(2339, 2213)
q = p * 7863
print(q)