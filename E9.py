class ComplexNo:
   def __init__(self, real, imag):
      self.re = real
      self.im = imag

   def __add__(self, o):
      return Complex(self.re+o.re, self.im+o.im)


def solve(comp1, comp2):
   print(comp1 + comp2)

comp1 = Complex(2, 3)
comp2 = Complex(5, -2)
solve(comp1, comp2)