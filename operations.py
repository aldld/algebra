# evaluate() function returns the result of applying the binary operation
# to two constants.

class Sum():
    def __init__(self, addend, augend):
        self.addend = addend
        self.augend = augend
    
    def evaluate(self):
        return self.addend + self.augend

class Difference():
    def __init__(self, minuend, subtrahend):
        self.minuend = minuend
        self.subtrahend = subtrahend
    
    def evaluate(self):
        return self.minuend - self.subtrahend

class Product():
    def __init__(self, mutiplicand, multiplier):
        self.multiplicand = multiplicand
        self.multiplier = multiplier
    
    def evaluate(self):
        return self.multiplicand * self.multiplier

class Quotient():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def evaluate(self):
        return self.numerator / self.denominator

class Exponent():
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent
    
    def evaluate(self):
        return base ** exponent

# Operation table
operations = {
    # '<symbol>': <class-name>
    '+': Sum,
    '-': Difference,
    '*': Product,
    '/': Quotient,
    '^': Exponent
}
