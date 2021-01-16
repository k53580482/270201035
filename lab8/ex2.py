a = int(input("Enter first integer :\n "))
b = int(input("Enter second integer :\n "))

def is_prime(x):
    for i in range(2, x):
        if x % i == 0 :
            return "Not prime!"
    else:
        return "Prime!"

print(is_prime(a))
print(is_prime(b))

def print_primes_between(x, y):
    if y > x :
        for i in range(x+1, y) :
            if is_prime(i) == "Prime!" :
                print(i)
    if x > y :
        for i in range(y+1, x) :
            if is_prime(i) == "Prime!" :
                print(i)

print_primes_between(a, b)
