openfile = open("./input1A.txt", "r")
outpt = open("./output1A.txt", "w")

readfile = openfile.readlines()

n, target = [int(i) for i in readfile[0].split()]

numbers = [int(i) for i in readfile[1].split()]

machedSum = False
for i in range(n - 1):
    if machedSum:
        break
    num_1 = int(numbers[i])
    for j in range(i+1, len(numbers)):
        num_2 = int(numbers[j])
        if num_1 + num_2 == target:
            machedSum = True
            break
if not machedSum:
    outpt.writelines(f"IMPOSSIBLE")
else:
     outpt.writelines(f"{i} {j+1}")