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
    
openfile = open('./input1.txt', 'r')
readfile = openfile.readlines()
outputfile = open('./output1.txt', "w")
# new = []
data = readfile[1]
# print(data)
data = [int(i) for i in data.split()]
mergeSort(data)
# print(new_arr)

[outputfile.write(f"{i} ") for i in new_arr]
outputfile.close()