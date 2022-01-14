import sys
args = sys.argv
print("Binary Search")
#index: 0  1  2  3  4  5   6   7   8   9  10  11  12
list = [0, 1, 3, 6, 8, 9, 10, 12, 14, 15, 16, 19, 20]
print(f'list: {list}')

#target = 20 # the value we are trying to find in the list
target = int(args[1])
print(f'target: {target}')
listLength = len(list)
minPosition = 0
maxPosition = listLength - 1
step = 0
while step < 1000:
    step += 1
    midPosition = (maxPosition + minPosition) // 2  # calculate average of max and min to find mid
    midValue = list[midPosition]
    print(f"\n---------------Step #{step}---------------")
    print(f"minPosition: {minPosition}")
    print(f"maxPosition: {maxPosition}")
    print(f"midPosition in list: {midPosition}")
    print(f"midValue in list:    {midValue}")

    if target == midValue:
        print(f"Good job, you've found the number {target} at midPosition {midPosition} after {step} step(s)")
        break
    if minPosition == maxPosition and target != midValue:
        print(f"The number {target} is not in the list")
        break
    
    elif midValue > target:
        print(f"current value ({list[midPosition]}) is larger than target ({target})")
        print("we need to look in the lower half")

        # calculate maxPosition
        maxPosition = midPosition - 1

    else:
        print(f"current value ({list[midPosition]}) is smaller than target ({target})")
        print("we need to look in the upper half")

        # calculate minPosition
        minPosition = midPosition + 1

