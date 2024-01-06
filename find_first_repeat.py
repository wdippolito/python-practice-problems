def find(A, target):
    low = 0
    high = len(A) -1

    while low <= high:
        mid = (low+high) // 2

        #if mid is greater than target, take left half high = mid -1
        #elif mid is less than target, take right half, low = mid +1
        #else:
            #if mid - 1 < 0 then return mid - at left end of list, therefor its first occurence
            #if stepping one index left of mid != target, then return mid, else take left half, high =mid -1
        if A[mid] > target:
            high = mid - 1
        elif A[mid] < target:
            low = mid + 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid -1] != target:
                return mid
            high = mid -1




A = [1,16,35,44,55,76,77,108,133,333,555,700]
print(find(A, 108))