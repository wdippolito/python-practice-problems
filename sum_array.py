arr = list(range(0,102,2))
from collections import Counter
for i in range(len(arr)):
    if i%2 == 1:
        arr[i] += i
    arr[1] = 4
count = Counter(arr)
min_count = max(count.values())
print(arr)
print(min_count)
print(sum(arr,sum(arr)))


arr[12] = 0
arr[0] = 1
arr[50] = 0
max = arr[0]
min = arr[0]
maxindex = 0
min_index = 0
print(arr)
for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]
        maxindex = i
    print(max, maxindex)
    if min > arr[i]:
        min = arr[i]
        min_index = i
    print(min, min_index)

profit = 0
if maxindex > min_index:
    profit = max - min
    print(profit)

arr.sort()
print(arr[-2])