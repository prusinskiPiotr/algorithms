def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, otherfraction):
        newnum = (self.num * otherfraction.den) + (self.den * otherfraction.num)
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newnum = (self.num * other.den) - (self.den * other.num)
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
        
    def __lt__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return num < den

    def __gt__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return num > den


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1 < f2)
print(f1 == f2)
print(f1 > f2)
