def hailstone(x):
    if x == 1 :
        return str(int(x))
    else :
        if x % 2 == 0:
            return str(int(x)) + "," + hailstone(x/2)
        else :
            return str(int(x)) + "," + hailstone(3*x + 1)

print(hailstone(11))
