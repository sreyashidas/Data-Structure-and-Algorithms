def fib(n,cache={}):
    if n <= 1 :
        return n
    elif n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
    
a = fib(6)
print(a)
