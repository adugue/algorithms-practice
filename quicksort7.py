from time import process_time 
import random

# Get the median of three of the array, changing the array in the process
def median(arr, mid, end):
    if arr[end] < arr[0]:
        arr[0], arr[end] = arr[end], arr[0]
    if arr[mid] < arr[0]:
        arr[0], arr[mid] = arr[mid], arr[0]
    if arr[end] < arr[mid]:
        arr[mid], arr[end] = arr[end], arr[mid]
    return arr[mid]

def quicksort(array):
    length = len(array)
    if length < 2:
        return array
    else:
        mid = (length - 1) // 2

        pivot = median(array, mid, length - 1) # use the "median of three" as the pivot

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

#print([random.randrange(0, 1000, 1) for i in range(30)])
