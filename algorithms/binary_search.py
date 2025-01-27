import math 
'''
	Binary search: Given a sorted list, find where an element is located at. 
	Start in the middle and determine if it's lower, higher, or equal to your
	element.

	If element = middle 
		return middle 
	If element  > middle 
		min = middle  + 1
	if element  < middle
		max = middle - 1

	Iterate through the list until element = middle, else return None. (Not in list)

'''
def binary_search(arr:list, val) -> int:
	n = len(arr)

	l = 0
	r = n - 1 

	while l <= r:
		m = (l + r) // 2
		x = arr[m]

		if x == val:
			return m
		if x > val:
			r = m - 1
		if x < val:
			l = m + 1
	return None

if __name__ == '__main__':
	nums = [12, 14, 2, 5, 7, 6]
	nums.sort()

	x = 7
	ans = binary_search(nums, x)
	print(nums)
	print(ans)