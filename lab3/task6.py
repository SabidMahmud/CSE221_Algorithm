def find_kth_smallest(arr, start, end, k):
  if start == k:
    return arr[start - 1]
  else:
    p = partition(arr, start, end)
    if p == k:
      return arr[p - 1]
    elif p < k:
      return find_kth_smallest(arr, start + 1, end, k)
    else:
      return find_kth_smallest(arr, start, end - 1, k)

def partition(arr, start, end):
  pivot = arr[end]
  p_index = start

  for i in range(start, end):
    if arr[i] <= pivot:
      arr[i], arr[p_index] = arr[p_index], arr[i]
      p_index += 1

  arr[end], arr[p_index] = arr[p_index], arr[end]
  return p_index

inputfile = open("./input6.txt", 'r')
output_file = open("./output6.txt", "w")

length = inputfile.readline().split()
length = int(length[0].strip())
arr = [int(i) for i in inputfile.readline().split()]

total_queries = int(inputfile.readline().split()[0])

for i in range(total_queries):
  k = int(inputfile.readline())
  number = find_kth_smallest(arr, 0, length - 1, k)
  output_file.write(f"{number}\n")