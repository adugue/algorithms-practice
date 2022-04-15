from time import process_time 
import random

def quicksort(array):
    length = len(array)
    if length < 2:
        return array
    else:
        randomIndex = random.randrange(0, length)
        pivot = array[randomIndex]
        smaller = []
        larger = []
        for i in range(randomIndex):
            if array[i] <= pivot:
                smaller.append(array[i])
            else:
                larger.append(array[i])

        for i in range(randomIndex + 1, length):
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
