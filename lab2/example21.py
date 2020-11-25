p = "abc123"
a = input("Password : ")

while a != p :
  if a == "help" :
    print(p[0])
  
  else :
    print("Wrong!")
  a = input("New Password : ")

if a == p :
    print("Welcome!")