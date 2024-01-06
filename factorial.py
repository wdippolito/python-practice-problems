factorial = 1
num = 5

if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("factorial is 1")
else: # find factorial
    for i in range(1,num+1):
        factorial = factorial * i
        print(factorial)
print(f"Factorial of {num} is {factorial}")

