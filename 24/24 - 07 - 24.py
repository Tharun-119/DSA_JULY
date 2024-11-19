arr1 = [1,2,4,8,9,12,14,18]
k1 = 12

def linear_search(arr,k):
    for i,v in enumerate(arr):
        if v == k:
            return i,v
print(linear_search(arr1, k1))



def binary_search(arr, k):
    
    lb = 0
    rb = len(arr)-1
    
    while lb <= rb:
        mid = lb + (rb - lb) // 2
        if k == arr[mid]:
            return mid 
        elif k < arr[mid]:
            rb = mid - 1
        else:
            lb = mid + 1
    return -1
    
print(binary_search(arr1,k1))



# swapping two numbers

a1 = 10
b1 = 45

def swap(a,b):
    # temp = a
    # a = b
    # b = temp
    a = a + b
    b = a - b
    a = a - b
    return a , b
print(swap(a1, b1))


max item in a array
arr1 = [8,2,3,4,7,89,12]

def maxi(arr):
    mx_value = arr[0]
    for i in arr:
        if i > mx_value:
            mx_value = i
    return mx_value
print(maxi(arr1))



# arr1 = [5,1,4,2,8]

def bubble_sort(arr):
    for j in range(len(arr)-1, 0 ,-1):  
        # (4, 0, -1) --> (4, 3, 2, 1)
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i] = arr[i] + arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] - arr[i+1]
    return arr
print(bubble_sort(arr1))



# set 3 
# Find the kth smallest element in an unsorted list
arr1 = [1,5,2,6,8,3]
k1 = 4
output = 5

def smallest(arr, k):
    arr = sorted(arr)
    return arr[k-1]
print(smallest(arr1, k1))


# Find the first non-repeating character in a string  

str1 = "swwtiysfs"
# output = w

def non_repeat_cha(a):
    dic = {}
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in a:
        if dic[i] == 1:
            return i
        
print(non_repeat_cha(str1))



# k th largest element in a unsorted array
arr1 = [1,5,2,9,5,8,3]
k1 = 4

def largest(arr,k):
    arr = list(set(sorted(arr)))
    return arr[-k]
print(largest(arr1,k1))


    
sum of all numbers in array using recurison
# arr1 = [1, 2, 3, 4, 5]

# def recursive_add(arr):
#     temp = 0
#     for i in arr:
#         temp+=i
#     return temp
# print(recursive_add(arr1))


# Palindrome
a1 = "racear"
def palindrome(a):
    i = 0
    j = len(a) - 1
    while i <= j:
        if a[i] == a[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

print(palindrome(a1))

method 2
s1 = "racecar"
def palin(s):
    for i in range(0,len(s)):
        if s[i] != s[-i-1]:
            return False
    return True
print(palin(s1))

#remove duplicates
def remove_duplicate(s):
    s = set(s)
    return list(s
print(remove_duplicate(s1))

method 2
s1 = [1,2,2,3,4,4,5]

def remove(s):
    result = []
    for i in s:
        if i not in result:
            result.append(i)
    return result
print(remove(s1))
