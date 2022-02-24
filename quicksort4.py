from time import process_time 
import random

def quicksort(array):
    length = len(array)
    if length < 2:
        return array
    else:
        mid = (length - 1) // 2
        pivot = array[mid]
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
