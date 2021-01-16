def sum_list(a_list, a = 0):
    if a == len(a_list) - 1 :
        if isinstance(a_list[a], list) == True :
            return sum(a_list[a])
        else :
            return a_list[a]
    else :
        if isinstance(a_list[a], list) == True :
            return sum(a_list[a]) + sum_list(a_list, a = a + 1)
        else :
            return a_list[a] + sum_list(a_list, a = a + 1)

print(sum_list([1,2,[8,3],3,[4,5,7],6]))