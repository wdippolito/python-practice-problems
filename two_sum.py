

def two_sum_brute(A,target):
    for i in range(0,len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])

def two_sum(A, target):
    i = 0
    j = len(A) -1

    while i < j:
        if A[i] + A[j] == target:
            return True
        elif A[i] + A[j] > target:
            j = j -1
        else:
            i += 1
    return False


A = [3,5,2,0,0,11]
A.sort()
target = 99
print(two_sum(A,target))