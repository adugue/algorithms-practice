from time import process_time 
import random

def quicksort(array):
    length = len(array)
    if length < 2:
        return array
    else:
        mid = (length - 1) // 2
        pivot = array[mid]
        smaller = [x for x in array[:mid] if x <= pivot] + \
                [x for x in array[mid + 1:] if x <= pivot]
        larger = [x for x in array[:mid] if x > pivot] + \
                [x for x in array[mid + 1:] if x > pivot]
        sortedSmaller = quicksort(smaller)
        sortedLarger = quicksort(larger)
        newArray = sortedSmaller + [pivot] + sortedLarger
        return newArray


start = process_time() 
for i in range(100000):
	res = [random.randrange(0, 1000, 1) for i in range(30)]
	quicksort(res)
end = process_time()
time = end - start
print(time)
