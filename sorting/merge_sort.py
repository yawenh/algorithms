# Merge Sort:

## Recursive implementation:
## Time Complexity: T(n) = 2*T(n/2) + cn

def merge(arr, start, end, mid):
	if (end - start <= 1):
		return
	if (mid - start <= 0 or end - mid <= 0):
		return
	i, j = start, mid
	temp = []
	while (i < mid and j < end):
		if (arr[i] < arr[j]):
			temp.append(arr[i])
			i = i + 1
		else:
			temp.append(arr[j])
			j = j + 1

	while (i < mid):
		temp.append(arr[i])
		i = i + 1
	while (j < end):
		temp.append(arr[j])
		j = j + 1

	for k in range(len(temp)):
		arr[start+k] = temp[k]


def merge_sort(arr, start, end):
	if (end - start <= 1):
		return
	mid = start + (end - start) // 2
	merge_sort(arr, start, mid)
	merge_sort(arr, mid+1, end)
	merge(arr, start, end, mid)

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	merge_sort(arr, 0, len(arr))
	for i in range(len(arr)):
		print (arr[i])

