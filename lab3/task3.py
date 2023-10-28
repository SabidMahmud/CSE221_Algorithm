def merge(n, m):
    i, j = 0, 0
    global new_arr
    new_arr = []
    # print(n, m)
    while i < len(n) and j < len(m):
        if n[i] < m[j]:
            new_arr.append(n[i])
            i += 1
        elif n[i] > m[j]:
            new_arr.append(m[j])
            j += 1
        else:
            new_arr.append(m[j])
            new_arr.append(n[i])
            j += 1
            i += 1

    while i < len(n):
        new_arr.append(n[i])
        i += 1

    while j < len(m):
        new_arr.append(m[j])
        j += 1

    return new_arr
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        # print(mid)
        a1 = mergeSort(arr[:mid])
        # print(a1)
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
# Merge sort function from task1


openfile = open("./input3.txt", "r")
readfile = openfile.readlines()

arr = [int(i) for i in readfile[1].split()]

new = []
for i in arr:
    new.append(int(i))
sortedArr = mergeSort(new)

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

count=0
length=len(sortedArr)
for i in new:
    indx = binarySearch(sortedArr, i)
    count += indx
    sortedArr.pop(indx)

outfile = open("./output3.txt", "w")
outfile.writelines(f"{count}")