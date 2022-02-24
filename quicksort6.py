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
        pivot = pivot = median(array, mid, length - 1) # use the "median of three" as the pivot
        smaller = []
        larger = []
        for i in range(mid):
            if array[i] <= pivot:
                smaller.append(array[i])
            else:
                larger.append(array[i])

        for i in range(mid + 1, length):
            if array[i] <= pivot:
                smaller.append(array[i])
            else:
                larger.append(array[i])
        newSmaller = quicksort(smaller)
        newLarger = quicksort(larger)
        newArray = newSmaller + [pivot] + newLarger
        return newArray

start = process_time() 
for i in range(100000):
	res = [random.randrange(0, 1000, 1) for i in range(30)]
	quicksort(res)
end = process_time()
time = end - start
print(time)

#print([random.randrange(0, 1000, 1) for i in range(30)])
