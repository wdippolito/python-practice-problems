def find_closest(A, target):
    low = 0
    high = len(A) -1
    right_diff = left_diff = min_diff = float('inf')
    closest = None

    # edge cases for empty list or single element
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    while low <= high:
        mid = (low+high) // 2
        if mid + 1 < len(A):
            right_diff = abs(A[mid+1] - target)
        if mid > 0:
            left_diff = abs(A[mid-1] - target)

        if left_diff < min_diff:
            min_diff = left_diff
            closest = A[mid - 1]
        if right_diff < min_diff:
            min_diff = right_diff
            closest = A[mid +1]
        
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid -1
            if high < 0:
                return A[mid]
        else:
            return A[mid]
    return closest






A1 = [1,3,5,7,8,11,21]
A2 = [3,5,45,54,111]

print(find_closest(A1, 9))
print(find_closest(A2, 25))