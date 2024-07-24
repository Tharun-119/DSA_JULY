# sum of all numbers in array using recurison
arr1 = [1, 2, 3, 4, 5]

def recursive_add(arr):
    temp = 0
    for i in arr:
        temp+=i
    return temp
print(recursive_add(arr1))
