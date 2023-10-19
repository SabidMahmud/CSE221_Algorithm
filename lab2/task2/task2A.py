openfile = open("./input2A.txt", "r")
readfile = openfile.readlines()

arr1 = [int(i) for i in readfile[1].split()]
arr2 = [int(i) for i in readfile[3].split()]

l1 = int(readfile[0])
l2 = int(readfile[2])
sortedlist = []
i, j = 0, 0
 
while i < l1 and j < l2:
    if int(arr1[i]) < int(arr2[j]):
        sortedlist.append(int(arr1[i]))
        i += 1
 
    else:
        sortedlist.append(int(arr2[j]))
        j += 1

sortedlist = sortedlist + arr1[i: ] + arr2[j: ]
# print(sortedlist)

writefile = open("./output2A.txt", "w")
[writefile.writelines(f"{i} ") for i in sortedlist]
writefile.close()