gpa = float(input("GPA : "))
num_of_lec = int(input("Number of lectures ? :"))

if gpa < 2.0 and num_of_lec < 47 :
    print("Failed !")

elif gpa >= 2.0 and num_of_lec < 47 :
    print("Failed !")

elif num_of_lec >= 47 and gpa < 2.0 :
    print("Failed !")

else :
    print("GRADUATED !")