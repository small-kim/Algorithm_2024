class Lab01:
	def power2(n):
		res = 1
		for i in range(n):
			res *= 2
		return res

	def power2a(self, n):
		if n == 0:
			return 1
		else:
			return 2 * self.power2a(n-1)

	def power2b(self, n):
		if n == 0:
			return 1
		else:
			return self.power2b(n-1) + self.power2b(n-1)

	def power2c(self, 2, n):
		if n == 0:
			return 1
		if n % 2 == 1:
			return 2 * self.power2c(n//2) * self.power2c(n//2)
		return self.power2c(n//2) * self.power2c(n//2)

	def powerxb(self, x, n):
		res = 1
		i = 0
		while i < n:
			res = x * res
			i = i + 1
		return res

	def powerxa(self, x, n):
		if n == 0:
			return 1
		if n % 2 == 1:
			return x * self.powerxa(x, n//2) * self.powerxa(x, n //2)
		return self.powerxa(x, n//2) * self.powerxa(x, n//2)

	def fib2(self, n):
		f = [0, 1]
		for i in range(2, n):
			f.append(f[i - 2] + f[i - 1])
		return f[n]

	def Hanoi(self, n, src, aux, tgt):
		if n == 1:
			print(f'move {n} from {src} to {tgt}')
			return
		else:
			Hanoi(n - 1, src, tgt, aux)
			print(f'move {n} from {src} to {tgt}')
			Hanoi(n - 1, aux, src, tgt)

	def gcdItr(self, a, b):
		while b > 0:
			a, b = b, a % b # r = a % b, a = b, b = r
		return a

	def gcdRec(self, a, b):
		if b == 0:
			return a
		else:
			return self.gcdRed(b, a % b)
