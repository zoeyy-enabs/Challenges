class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a 
        self.b = b 
        self.p = p 

class Point:
    def __init__(self, x=False, y=False):
        self.x = x 
        self.y = y 
        self.o = not (type(x) == int and type(y) == int)

    def __eq__(self, q): 
        return (self.x == q.x and self.y == q.y) or (self.o and q.o)
    def __ne__(self, q): 
        return not (self == q)

    def __str__(self):
        return (f"Point({self.x},{self.y})" if not self.o else "Point(O)")