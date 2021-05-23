# Fn = Fn-1 + Fn-2
# n=>2
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib_generator(n):
    i = 0
    while i < n:
        yield fib(i)
        i += 1