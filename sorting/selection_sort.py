# Selection Sort:

## I. Iterative version: O(n^2)

def selection_sort_iter(arr):
	for i in range(len(arr)):
		min_element = i
		cur = i
		while (cur < len(arr)):
			if (arr[cur] < arr[min_element]):
				min_element = cur
			cur = cur + 1

		temp = arr[i]
		arr[i] = arr[min_element]
		arr[min_element] = temp

## II. Recursion version: 
# Time Complexity: T(n) = T(n-1) + cn 

# Linear search to find the minimal element: cn
def min_pos(arr, start, end):
	min_pos = start
	for i in range(start, end):
		if (arr[i] < arr[min_pos]):
			min_pos = i
	return min_pos

# Recursive call:
def selection_sort_recur(arr, start, end):
	if (end - start <= 1):
		return
	min_p = min_pos(arr, start, end)
	temp = arr[min_p]
	arr[min_p] = arr[start]
	arr[start] = temp
	selection_sort_recur(arr, start+1, end) 

# Print an array
def print_array (arr):
	for i in range(len(arr)):
		print(arr[i])
	print(" ")


if __name__ == '__main__':
	arr1 = [-5, 6, 7, 1, -100, 4, 6, -7]
	selection_sort_recur(arr1, 0, len(arr1))
	print_array(arr1)

	arr2 = [4, 2, 6, 7, 1, 3]
	selection_sort_iter(arr2)
	print_array(arr2)
	

