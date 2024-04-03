class Num01:
	def A(arr):
		max_sum = float('-inf')
		n = len(arr)
		for i in range(n):
			current_sum = 0
			for j in range(i, n):
				current_sum += arr[j]
				max_sum = max(max_sum, current_sum)
		return max_sum

	def B(arr):
		if len(arr) == 1:
			return arr[0]

		mid = len(arr) // 2

		left_sum = B(arr[:mid])
		right_sum = B(arr[mid:])

		left_max = float('-inf')
		right_max = float('-inf')
		temp_sum = 0

		for i in range(mid, len(arr)):
			temp_sum += arr[i]
			right_max = max(right_max, temp_sum)

		temp_sum = 0
		for in range(mid - 1, -1, -1):
			temp_sum += arr[i]
			left_max = max(left_max, temp_sum)

		mid_sum = left_max + right_max

		return max(left_sum, right_sum, mid_sum)

	def C(arr):
		max_sum = arr[0]
		current_sum = arr[0]
		for i in range(1, len(arr)):
			current_sum = max(arr[i], current_sum + arr[i])
			max_sum = max(max_sum, current_sum)
		return max_sum

class Num02:
	def power_set(L, n):
		if n == 0:
			return [[]]
		else:
			subsets = power_set(L, n - 1)
			T = [subset + [L[n - 1]] for subset in subsets]
			return subsets + T

	def intersection(A, B):
		C = set()
		for a in A:
			for b in B:
				if a == b:
					C.add(a)
					break
		return C

	def bc(n, k):
		B = [[0] * (k + 1) for _ in range(n + 1)]
		for i in range(n + 1):
			for j in range(min(i, k) + 1):
				if j == 0 or j == i:
					B[i][j] = 1
				else:
					B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
		return B

	def compute_integral_matrix(M):
		n = len(N)
		m = len(M[0])
		S = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + M[i - 1][j - 1]
		return S

	def find_max_zero_sum_submatrix(M):
		n = len(M)
		m = len(M[0])
		S = compute_integral_matrix(M)
		maxMS = 0
		rowStart = rowEnd = colStart = colEnd = 0

		for r1 in range(n):
			for r2 in range(r1, n):
				for c1 in range(m):
					for c2 in range(c1, m):
						ssum = S[r2 + 1][c2 + 1] - S[r2 + 1][c1] - S[r1][c2 + 1] + S[r1][c1]
						MS = (r2 - r1 + 1) * (c2 - c1 + 1)
						if ssum == 0 and MS > maxMS:
							maxMS = MS
							rowStart, rowEnd, colStart, colEnd = r1, r2, c1, c2

		return [row[rowStart:rowEnd + 1] for row in M[colStart:colEnd + 1]]

	def string_matching(T, P):
		n = len(T)
		m = len(P)
		for i in range(n - m + 1):
			j = 0
			while j < m and P[j] == T[i + j]:
				j += 1
			if j == m:
				return i
		return -1

	import math
	def closest_pair(P):
		n = len(P)
		d = float('-inf')
		for i in range(n - 1):
			for j in range(i + 1, n):
				d = min(d, math.sqrt((P S[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2))
		return d
