# find the maximum number in an array using recursion (d&c)
# first approach
def max(arr):
    if len(arr) == 1:
        return arr[0]
    rest = max(arr[1:])
    if arr[0] > rest:
        return arr[0]
    else:
        return rest

print(max([2, 4, 6, 1, 12, 3]))


# find the maximum number in an array using recursion (d&c)
# second approach
def max2(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1] 
    rest = max2(arr[1:])
    return arr[0] if arr[0] > rest else rest

print(max2([2, 4, 6, 1, 12, 3]))
