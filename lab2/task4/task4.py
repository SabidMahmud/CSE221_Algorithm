openfile = open("./input4.txt", "r")
N, M = map(int, openfile.readline().split())
activities = [list(map(int, line.strip().split())) for line in openfile.readlines()]


def custom_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_subarr = arr[:mid]
    right_subarr = arr[mid:]

    left_subarr = custom_merge_sort(left_subarr)
    right_subarr = custom_merge_sort(right_subarr)

    sorted_arr = []
    i = j = 0

    while i < len(left_subarr) and j < len(right_subarr):
        if left_subarr[i][0] < right_subarr[j][0]:  
            sorted_arr.append(left_subarr[i])
            i += 1
        else:
            sorted_arr.append(right_subarr[j])
            j += 1

    sorted_arr.extend(left_subarr[i:])

    sorted_arr.extend(right_subarr[j:])

    return sorted_arr


def max_activities(N, M, activities):
    activities = custom_merge_sort(activities)
    # print(activities)
    count = 0
    start_time, end_time = activities[0]
    c = 1
    d = 0
    for i in range(N * M):
        if d == M:
            break
        else:
            if c < len(activities):
                if activities[c][0] >= end_time:
                    start_time, end_time = activities[c]

                    # print("inif ", c)
                    # print(activities[c])
                    activities.pop(c)
                    count += 1
                else:
                    c += 1
            else:
                d += 1
                c = 0
                # print("before pop", activities)
                activities.pop(0)
                count += 1
                # print("count in else ", count)
                if len(activities) == 0:
                    break
                else:
                    start_time, end_time = activities[0]

    return count




result = max_activities(N, M, activities)
output = open("./output4.txt", "w")
output.write(str(result))
output.close()
