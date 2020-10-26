a = float(input("Enter number 1 : "))
b = float(input("Enter number 2 : "))
c = float(input("Enter number 3 : "))

if a <= b and a <= c :
    result = a

elif b < a and b < c :
    result = b

else :
    result = c


print(result)