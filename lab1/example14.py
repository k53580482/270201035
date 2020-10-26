day = int(input("Which Number of Day are you in ? : "))
month = int(input("Which Number of Month are you in ? : "))


if month >= 9 and month <= 12:
    if month == 9 and day < 22 :
        print("Summer!")
    elif month == 12 and day >= 21 :
        print("Winter!")
    else :
        print("Fall!")

elif month <= 3 :
    if month == 3 and day >= 20 :
        print("Spring!")
    else :
        print("Winter")

elif month >= 3 and month <= 6 :
    if month == 6 and day >= 21 :
        print("Summer!")
    else :
        print("Spring!")

elif month >= 6 and month <= 9 :
    if month == 9 and day >= 22 :
        print("Winter!")
    else :
        print("Fall!")