def fixed(A):
    low = 0 
    high = len(A)-1

    while low <= high:
        mid = (low + high) // 2 #mid is equal to the index
        if A[mid] < mid: #if value at mid index less than index 
            low = mid +1
        elif A[mid] > mid:
            high = mid -1
        else:
            return A[mid]
    return None

A1 = [0,3,3,5,9,11,13]
print(fixed(A1))