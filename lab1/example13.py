a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

delta = ( b ** 2) - ( 4 * a * c)
r1 = ( -b + ( delta ** 0.5 )) / (2 * a)
r2 = ( -b - ( delta ** 0.5 )) / (2 * a)


if delta > 0 :
    print("There are 2 real roots!")
    print ("-->" , r1)
    print ("-->" , r2)

elif delta < 0 :
    print("There are no real root!")


else :
    print("There is 1 real root!")
    print("-->" , r1)