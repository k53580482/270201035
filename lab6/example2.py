a = int(input("How many students : "))

for i in range(1, a+1) :
  mt1 = float(input("mt1 ="))
  mt2 = float(input("mt2 ="))
  f = float(input("f ="))
  grade = mt1 * 0.3 + mt2 * 0.3 + f * 0.4
  print("Student", i , ":" , grade)




