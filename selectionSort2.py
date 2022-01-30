def smallestIndex(arr): # finds the smallest index in an array
    minVal = arr[0]
    minIndex = 0
    for i in range(len(arr)):
        if minVal > arr[i]:
            minVal = arr[i]
            minIndex = i
    return minIndex 

def selectionSort(arr):
    sorted = [] 
    for i in range(len(arr)):
        sorted.append(arr.pop(smallestIndex(arr)))
    return sorted

print(selectionSort([0, 7, 3, 2, 9, 1]))
print(selectionSort([123, 54, -13, 0, 7, 3, 2, 9, 1]))
