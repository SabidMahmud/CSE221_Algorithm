def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            # if smaller than pivot, then swap.
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    #swaping pivot with i-th element.
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i + 1 #partition index
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        #recursion for the left
        quickSort(array, low, pi - 1)
        #recursion for the right
        quickSort(array, pi + 1, high)

openfile = open("./input5.txt", "r")
readfile = openfile.readlines()
array = [int(i) for i in readfile[1].split()]
quickSort(array, 0, int(readfile[0])-1)
print(array)