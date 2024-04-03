def UE(arr):
	n = len(arr)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if arr[i] == arr[j]:
				return False
	return True

def GE(A):
	n = len(A)
	for i in range(n - 1):
		for j in range(i + 1, n):
			for k in range(i, n):
				A[j][k] -= A[i][k] * A[j][i] / A[i][i]
		return A

def binRec(n):
	if n == 1:
		return 1
	else:
		return binRec(n // 2) + 1

