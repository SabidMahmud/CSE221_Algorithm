inpt = open("./input4.txt","r")
readfile = inpt.readlines()
arr = [int(i) for i in readfile[1].split()]

def merge(a, b):
    list1 = a
    list2 = b
    len_1 = len(a)
    len_2 = len(b)
    merged = []
    p, q = 0, 0

    while p < len_1 and q < len_2:
        if list1[p][0] < list2[q][0]:
            merged.append(list1[p])
            p += 1
        else:
            merged.append(list2[q])
            q += 1

    merged.extend(list1[p:])
    merged.extend(list2[q:])

    return merged

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


def maxSum(arra):
    squared_val = [(val**2, idx) for idx, val in enumerate(arra)]
    squared_val = mergeSort(squared_val) 
    i, j = 0, len(arra) - 1
    maximum = float('-inf')
    while i < j:
        if squared_val[j][1] <= i:
            j -= 1            
        sum = arra[i] + squared_val[j][0]
 
        maximum = max(maximum, sum)
        i += 1
    return maximum

outfile = open("./output4.txt", "w")
outfile.writelines(f"{maxSum(arr)}")