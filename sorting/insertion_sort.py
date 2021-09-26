# Insertion Sort:

def insertion_sort(arr, start, end):
	for i in range(end-start):
		j = i
		while (j > 0 and arr[j-1] > arr[j]):
			swap(arr, j-1, j)
			j = j - 1

def swap(arr, i, j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp

def print_array (arr):
	for i in range(len(arr)):
		print(arr[i])
	print(" ")


if __name__ == '__main__':
	arr = [3, 2 ,1, 5, 4]
	n = len(arr)
	insertion_sort(arr, 0, n)
	print_array(arr)
