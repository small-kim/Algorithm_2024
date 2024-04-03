class lab02:
	def ways1(self, n):
		if n == 1:
			return 1
		if n == 2:
			return 2
		if n == 3:
			return 3
		else:
			return self.ways1(n-1) + self.ways1(n-2)

	def ways2(self, n):
		ways = [1, 1]
		for i in range(2, n+1):
			ways.append(ways[i - 1] + ways[i - 2])
		return ways[n]

	def power(self, X, n):
		res = [[1, 0], [0, 1]] # identity matrix
		while n > 0:
			if n % 2 == 1:
				res = self.mul(res, X)
			X = self.mul(X, X)
			n = n // 2
		return res

	def mul(self, A):
		C = [[0, 0] for i in range(2)]
		for i in range(2):
			for j in range(2):
				C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]
		return C

	def ways3(self, n):
		M = [[1, 1], [1, 0]]
		res = self.power(M, n)
		print(res)
		return res[0]
