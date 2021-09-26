# Counting Sort:
# Suppose A consist of n integers all in {0, 1, .., k - 1}
# 1. Maintain an array B of length k intialized to all 0
# 2. Scan through A and increment B[A[i]]
# 3. Scan through B output i exactly B[i] times
def counting_sort(arr):
	n = len(arr)
	if n <= 1:
		return
	max_element = -1
	for i in arr:
		if max_element < i:
			max_element = i

	B = [0]*(max_element+1)

	for i in range(n):
		B[arr[i]] = B[arr[i]] + 1

	pos = 0
	for i in range(len(B)):
		j = B[i]
		while j > 0:
			arr[pos] = i
			pos = pos + 1
			j = j - 1

if __name__ == '__main__':

	arr = [5,6,7,3,2,2,8,7]
	counting_sort(arr)
	for i in arr:
		print(i)

