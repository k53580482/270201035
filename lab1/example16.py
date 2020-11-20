year = int(input("Which year are you in ? : "))

if year % 4 == 0 :
    if year % 100 == 0 and year % 400 == 0 :
        print ("Leap Year!")

    elif year % 4 == 0 :
        print ("Leap Year!")

    else :
        print ("Not Leap Year!")

else :
    print ("Not Leap Year!")