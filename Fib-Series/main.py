def fib(n):
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end = " ")
    for _ in range(n-2):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
    print()

    
fib(20)