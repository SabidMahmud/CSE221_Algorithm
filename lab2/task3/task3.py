openfile = open("./input3.txt", "r")
readfile = openfile.readlines()

def merge(arr1, arr2):
    p = len(arr1)           # length of array1
    q = len(arr2)           # length of array2
    marged = []
    i, j =0, 0
    while (i < p) and (j < q):
        if int(arr1[i].split()[1]) < int(arr2[j].split()[1]):
            marged.append(arr1[i])
            i += 1
        else:
            marged.append(arr2[j])
            j+=1
    marged = marged + arr1[i:] + arr2[j:]
    return marged

def merge_sort(arr):
    if len(arr) <= 1: return arr
    else:
        mid = len(arr) // 2
        a1 = merge_sort(arr[ : mid])
        a2 = merge_sort(arr[mid : ])
        return merge(a1, a2)
    
sortedarr = merge_sort(readfile[1:])
res = []

endtime = 0
count = 0
for i in sortedarr:
    startime = int(i.split()[0])
    if startime >= endtime:
        count += 1
        res.append(i)
        endtime = int(i.split()[1])

printfile = open("./output3.txt", "w")
printfile.writelines(f"{count}\n")
[printfile.writelines(f"{i}") for i in res]
printfile.close()