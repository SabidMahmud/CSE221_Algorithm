inputfile = open('./input3_1.txt', 'r')
outputfile = open('./output3_1.txt', 'w')
given = inputfile.readline().split()

N = int(given[0])
K = int(given[1])
rep = [0] * (N+1)
check = [1] * (N+1)

for i in range(N+1):
    rep[i] = i

for i in range(K):
    val = inputfile.readline()
    val = val.split()
    a = int(val[0])
    b = int(val[1])
    if rep[a] != rep[b]:
        check[rep[a]] += check[rep[b]]
        check[rep[b]] = check[rep[a]]
        print(check[rep[b]], file = outputfile)
        rep[b] = rep[a]
    else:
        print(check[rep[b]], file = outputfile)