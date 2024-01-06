to_swap = [5,3,66,3,2,1]

temp = to_swap[0]
to_swap[0] = to_swap[-1] 
to_swap[-1] = temp

print(to_swap)

get = (to_swap[0],to_swap[-1])
to_swap[-1],to_swap[0] = get
print(to_swap)