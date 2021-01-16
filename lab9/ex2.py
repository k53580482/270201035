def reversed(list, n = -1) :
    if int(n) + int(len(list)) == 0 :
        return list[n]
    else :
        return str(list[n]) + "," + str(reversed(list, n-1))

print(reversed([1,2,3,4,5,6,7,8,9]))