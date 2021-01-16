a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
def func1(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum ** 2
a = func1(a_list)
print(a)
