from collections import defaultdict
def result(locations, movedFrom, movedTo):
    result = locations.copy()

    m = defaultdict(int)

    for val in locations:
        m[val] = 1
    
    for i, val in enumerate(movedFrom):
        m[val] = 0
        m[movedTo[i]] = 1
    
    index = 0
    for key,val in m.items():
        if val == 1:
            result[index] = key
            index += 1
    
    result.sort()
    return result

loc = [1,7,6,8]
movedfrom = [1,7,2]
movedto = [2,9,5]


print(result(loc, movedfrom, movedto))