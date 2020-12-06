e1 = input("Employee 1's salary :")
e2 = input("Employee 2's salary :")
e3 = input("Employee 3's salary :")
e4 = input("Employee 4's salary :")
e5 = input("Employee 5's salary :")

employees = {
    "Employee 1": e1 ,
    "Employee 2": e2 ,
    "Employee 3": e3 ,
    "Employee 4": e4 ,
    "Employee 5": e5
}
a = employees.get("Employee 1")
b = employees.get("Employee 2")
c = employees.get("Employee 3")
d = employees.get("Employee 4")
e = employees.get("Employee 5")

lis = a, b, c, d, e
lis = sorted(list(lis))
lis.reverse()
print(lis[0:3])



