openfile = open("./input1B.txt", "r")
readlines = openfile.readlines()
n, target = [int(i) for i in readlines[0].split()]

nums = [int(i) for i in readlines[1].split()]
i = 0
j = n - 1
matchedSum = False
while not matchedSum:
    if i >= j:
        break
    sum = nums[i] + nums[j]
    if sum == target:
        matchedSum = True
    elif sum < target:
        i += 1
    else:
        j -= 1

printfile = open("./output1B.txt", "w")
if not matchedSum:
    printfile.writelines(f"IMPOSSIBLE")
else:
     printfile.writelines(f"{i+1} {j+1}")