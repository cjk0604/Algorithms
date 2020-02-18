def func(n):
    print(n)
    if n <= 1:
        return n
    
    if n % 2 == 1:
        return func((3*n) + 1)
    else:
        return func(n//2)

print(func(3))