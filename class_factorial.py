class Factorial:
	def __init__(self,n):
		self.n = self._factorial(n)
	def _factorial(self,n):
		fac = n
		for i in range(1,n):
			fac = fac*i
		return fac

a = Factorial(4)
print(a.n)