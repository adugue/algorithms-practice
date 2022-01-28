def findSmallestIndex(arr):
    minVal = arr[0]
    minIndex = 0
    for i in range(len(arr)):
        if minVal > arr[i]:
            minVal = arr[i]
            minIndex = i
    return minIndex 

def selectionSort(arr):
    length = len(arr)
    sorted = arr.copy()
    tempArr = arr.copy()
    for i in range(length):
        minIndex = findSmallestIndex(tempArr)
        minVal = tempArr[minIndex]
        sorted[i] = minVal
        if minIndex == 0:
            tempArr = tempArr[1:]
        elif minIndex == len(tempArr) - 1:
            tempArr = tempArr[:len(tempArr)-1]
        else:
            tempArr = tempArr[0:minIndex] + tempArr[minIndex+1:]
    return sorted

print(selectionSort([0, 7, 3, 2, 9, 1]))
print(selectionSort([123, 54, -13, 0, 7, 3, 2, 9, 1]))
