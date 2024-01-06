
def array_game(A):
    furthest = 0
    last_index = len(A) - 1
    i = 0
    while i <= furthest and furthest < last_index:
        furthest = max(furthest, A[i]+ i)
        i += 1
    return furthest >= last_index

A = [2,4,0,1,3,2,1]

print(array_game(A))
A = [2,4,0,0,0,0,0,1]
print(array_game(A))