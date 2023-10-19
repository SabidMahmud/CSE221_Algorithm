openfile = open('./input2.txt', 'r')
readfile = openfile.readlines()
outfile = open('./output2b.txt', 'w')
n = [int(i) for i in readfile[1].split()]
m = [int(i) for i in readfile[3].split()]
new_arr = []
def margeListSort(n, m, new_arr):
    i, j = 0, 0
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
    
margeListSort(n, m, new_arr)
[outfile.write(f"{i} ") for i in new_arr]

outfile.close()