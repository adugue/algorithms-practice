#import time
#start_time = time.time()

steps = 0
def addStep():
	global steps
	steps += 1


def quicksort(array):
    length = len(array)
    addStep()
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

a = [18, 15, 29, 23, 32, 19, 3, 1, 7, 54, 4, 9, 324, 23, 576, 987342, 56, 123, 34324, 67, 584, 22, 645, 345, 32, 7568, 5768, 245, 5674, 324, 56345, 634, 634565, 634535]
print(a)
print(quicksort(a))
print(steps)

#print("--- %s seconds ---" % (time.time() - start_time))
