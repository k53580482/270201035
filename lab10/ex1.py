def f(n, a = 1) :
    if a == 3 :
        return n
    else :
        return n + f(n, a = a + 1)

print(f(10))