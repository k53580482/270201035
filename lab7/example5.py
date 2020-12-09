password = input("Enter password : ")

while True:
    if len(password) < 8:
        print("Password should be minimum 8 characters long!")
        password = input("Please enter new password! : ")
    elif password.lower() == password :
        print("There should be at least 1 uppercase letter!")
        password = input("Please enter new password! : ")
    elif password.upper() == password :
        print("There should be at least 1 lowercase letter!")
        password = input("Please enter new password! : ")
    elif "0" not in password and "1" not in password and "2" not in password and "3" not in password and "4" not in password and "5" not in password and "6" not in password and "7" not in password and "8" not in password and "9" not in password :
        print("There should be at least 1 number!")
        password = input("Please enter new password! : ")
    else :
        print("True!")
        break
