# rewritten to use recursion (divide and conquer) instead of a while loop
import sys
args = sys.argv
print("Binary Search")
#index: 0  1  2  3  4  5   6   7   8   9  10  11  12
list = [0, 1, 3, 6, 8, 9, 10, 12, 14, 15, 16, 19, 20]
print(f'list: {list}')

target = int(args[1])
print(f'target: {target}')
print("-------------------------------")

def binSearch(arr):
    if len(arr) == 1:
        print(f"subarray: {arr}")
        if arr[0] == target:
            print(f"Good job, you've found the number {target}")
            return
        else:
            print(f"The number {target} is not in the list")
            return
    minPosition = 0 
    maxPosition = len(arr) - 1
    midPosition = (maxPosition + minPosition) // 2  # calculate average of max and min to find mid
    midValue = arr[midPosition]
    print(f"subarray: {arr}")
    print(f"midValue = {midValue}")
    print("---------------")
    if midValue == target:
        print(f"Good job, you've found the number {target}")
        return     
    else:
        if midValue > target:
            maxPosition = midPosition - 1
        else:    
            minPosition = midPosition + 1

        binSearch(arr[minPosition:maxPosition + 1])
        return

binSearch(list)
