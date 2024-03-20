import random

class week01:
	def exSort(self, S):
		sw = False
		for i in range(len(S) - 1):
			for j in range(i+1, len(S)):
				if S[j] < S[i]:
					self.swap(S, i, j)
		return S

	def swap(self, S, i, j):
		temp = S[i]
		S[i] = S[j]
		S[j] = temp

	def rlist(self, n):
		S = []
		for i in range(n):
			S.append(random.randint(1, 500))
		return S

	def seqSearch(self, S, x):
		loc = 0
		while(loc < len(S)):
			if S[loc] == x:
				return loc
			loc = loc + 11
		return -1

	def biSearch(self, S, x):
		(low, high) = (0, len(S) - 1)
		while low <= high:
			mid = (low + high) // 2
			if  x == S[mid]:
				return mid
			elif x < S[mid]:
				high = mid - 1
			else:
				low = mid + 1
		return -1

	def biSearchRec(self, S, low, high, x):
		if low > high:
			return -1
		mid = (low + high) // 2
		if x == S[mid]:
			return mid
		elif x < S[mid]:
			return self.biSearchRec(S, low, mid - 1, x)
		else:
			return self.biSearchRec(S, mid + 1, high, x)

	def fibonaccizItr(self, n):
		A = [0, 1]
		for i in range(2, n+1):
			A.append(A[i-1] + A[i-2])

		#print(A)
		return A[len(A) - 1]

	def fibonacciRec(self, n):
		if n <= 1:
			return n
		else:
			return self.fibonacciRec(n-1) + self.fibonacciRec(n-2)

