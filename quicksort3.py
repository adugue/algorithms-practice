steps = 0

def addStep():
	global steps
	steps += 1

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
    addStep()
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

a = [18, 15, 29, 23, 32, 19, 3, 1, 7, 54, 4, 9, 324, 23, 576, 987342, 56, 123, 34324, 67, 584, 22, 645, 345, 32, 7568, 5768, 245, 5674, 324, 56345, 634, 634565, 634535]

print(a)
print(quicksort(a))
print(steps)
