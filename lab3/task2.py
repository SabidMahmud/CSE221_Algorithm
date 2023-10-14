def devidenConquer(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2
        a1 = devidenConquer(arr[:mid])
        a2 = devidenConquer(arr[mid:])
        return (max(a1, a2))

openfile = open('./input2.txt', 'r')
readfile = openfile.readlines()
data = readfile[1].split()
data = [int(i) for i in data]
outputfile = open('./output2.txt', "w")
result = devidenConquer(data)
outputfile.write(str(result))