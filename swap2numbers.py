num1 = 10
num1 = int(input())
print(f"value of number 1: {num1}")
count = 0
for i in range(1, num1 +1):
    print(i)
    if num1%i == 0:
        count +=1
if count <= 2:
    print(num1, " is prime")    
else:
    print(num1, " is not prime")    