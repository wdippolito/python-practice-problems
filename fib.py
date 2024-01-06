#print fib seq

# n1 = 0
# n2 = 1

# for i in range(2, 10):
#     sum=n1+n2
#     print(sum)
#     n1 = n2
#     n2 = sum
fib_cache = {}

from functools import lru_cache

@lru_cache(maxsize=10000)
def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)
    # fib_cache[n] = value
    # return value

for i in range(1,12111):
    print(fib(i))