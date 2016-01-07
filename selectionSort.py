import random

sample_list = []

number = 0

while number < 100:
	sample_list.append(random.randint(0,10000))
	number += 1

def selection_sort(arr):
	for x in range(len(arr)):  			
		current_min = [x,arr[x]]
		for i in range(x,len(arr)):	
			if arr[i] < current_min[1]:
				current_min = [i,arr[i]]
		temp = arr[x]
		arr[x] = current_min[1]
		arr[current_min[0]] = temp
	print arr

selection_sort([39,5,9,12,43,24,25,26,2])