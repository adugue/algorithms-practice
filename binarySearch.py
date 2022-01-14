import sys
args = sys.argv
#print(args[1])

#index: 0  1  2  3  4  5   6   7   8   9  10  11  12
list = [0, 1, 3, 6, 8, 9, 10, 12, 14, 15, 16, 19, 20]

#target = 20 # the value we are trying to find in the list
target = int(args[1])
print(f'target: {target}')
listLength = len(list)
position = int(listLength / 2)
minPosition = 0
maxPosition = listLength - 1
i = 0
while True and i < 1000:
#for i in range(5):
    print("------------------------------------")
    print(f"***current position in list: {position}")
    print(f"***current value in list: {list[position]}")
    print(f"number of items in list: {listLength}")
    print(f"minPosition: {minPosition}")
    print(f"maxPosition: {maxPosition}")

    if target == list[position]:
        print(f"Good job, you've found the number {target} at position {position} after {i + 1} step(s)")
        break
    if listLength <= 1 and target != list[position]:
        print(f"The number {target} is not in the list")
        break
    
    elif list[position] > target:
        print(f"current value ({list[position]}) is larger than target ({target})")
        print("we need to look in the lower half")
        # update listLength (equal to the number of items in lower half)
        listLength = position - minPosition
        print(f'new listLength: {listLength}')
        # calculate maxPosition
        maxPosition = position - 1
        # calculate new position
        position = minPosition + int(listLength / 2) - 1
        if position < minPosition:
            position = minPosition
        print(f'new position {position}')

    else:
        print(f"current value ({list[position]}) is smaller than target ({target})")
        print("we need to look in the upper half")
        # update listLength (equal to the number of items in upper half)
        listLength = maxPosition - position 
        print(f'new listLength: {listLength}')
        # calculate minPosition
        minPosition = position + 1
        # calculate new position
        position = minPosition + int(listLength / 2) - 1
        if listLength % 2 > 0:
            position += 1
        if position < minPosition:
            position = minPosition
        print(f'new position {position}')

    i += 1
