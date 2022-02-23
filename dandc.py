# summing an array using a for loop
def sum(x):
    total = 0
    for i in x:
        total += i
    return total

print(sum([2, 4, 6]))


# summing an array using recursion (d&c)
def sum2(arr):
    if arr == []:
        return 0
    return arr[0] + sum2(arr[1:])

print(sum2([2, 4, 6]))


# counting items in a list using recursion (d&c)
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

print(count([2, 4, 6]))
