def plus_one(digits):
    n=len(digits)
    self=1
    for i in range(n):
        digits[n-1]=digits[n-1]+self
        return digits
digits=[9]
print(plus_one(digits))

