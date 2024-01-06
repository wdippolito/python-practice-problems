def find_peak(A):
    low = 0
    high = len(A) - 1

    if len(A) == 1:
        return A[0]
    if len(A) == 0:
        return None

    while low <= high:
        #if the left and right element are both less than mid, return mid.
        #if left is less and right is greater, then take right half and search
        #low = mid + 1
        #if left is greater and right is less, take left half and search
        #high = mid - 1
        #if you reach the end of the while loop then there is no peak.
        mid = (low+high) // 2

        #if accessing elements left and righht of mid, need to verify that they are in bounds of the list
        mid_left = A[mid - 1] if mid - 1 >=0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")
        
        if A[mid] > mid_right and A[mid] > mid_left:
            return A[mid]
        elif A[mid] > mid_left and A[mid] < mid_right:
            low = mid + 1
        elif A[mid] < mid_left and A[mid] > mid_right:
            high = mid -1


    return None


def find2(A, target):
    low = 0
    high = len(A) - 1

    # return if base or edge case ie len [0]
    while low <= high:
        mid = (low+high) // 2

        mid_left = A[mid -1] if mid -1 >= 0 else float('-inf')
        mid_right = A[mid+1] if mid +1 <= len(A) else float ('inf')

        #take left half to search
        # high = mid - 1

        #take right half to search
        # low = mid + 1

        #return condition

    #return not condition



A1 = [1,3,4,6,9,13,17,33,3,2,1]
A2 = [0,4,3,2,1]

print(find_peak(A1))