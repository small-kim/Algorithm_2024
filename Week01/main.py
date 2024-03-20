from week01 import week01
import time

def searchTest():
	w1 = week01()
	S = w1.rlist(10)
	print(S)
	x = 45
	stime = time.time()
	loc = w1.seqSearch(S, 45)
	print(" Time taken by Iterative Algorithm = {}".format(time.time() - stime))
	if loc != -1:
		print("{} is found at {}".format(x, loc))
	else:
		print("Could not found {}".format(x))

	stime = time.time()
	S1 = w1.exSort(S)
	print(S1)
	loc = w1.biSearchRec(S1, 0, len(S1) - 1, x)
	print(" Time taken by Recursive Algorithm = {}".format(time.time() - stime))
	if loc != -1:
		print("{} is found at {}".format(x, loc))
	else:
		print("Could not found {}".format(x))

def fibTest():
	w1 = week01()
	n = 35
	stime = time.time()
	print("{}th Fibonaaci term is {}".format(n, w1.fibonaccizItr(n)))
	print("Time taken by Iterative Algorithm = {:.5f}".format(time.time() - stime))


	stime = time.time()
	print("{}th Fibonaaci term is {}".format(n, w1.fibonaccizItr(n)))
	print("Time taken by Rcursive Algorithm = {:.5f}".format(time.time() - stime))

def main():
	print("This is week01...")
	searchTest()

if __name__ == "__main__":
	main()
