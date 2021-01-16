def secure(password):
    alphabetic = 0
    numeric = 0
    digit = 0
    total = 0

    if len(password) < 8 or " " in password:
        pass
    else :
        for i in password :
            if i.isalpha() == True :
                alphabetic += 1
            elif i.isnumeric() == True :
                numeric += 1
            else :
                digit += 1

    if alphabetic > 0 :
        total += 1
    if digit > 0 :
        total += 1
    if numeric > 0 :
        total += 1

    print(password, "Level", total)

def main():
    enter = input("Enter password:")
    secure(enter)

main()


