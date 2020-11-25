mail = str(input("What is your mail address : "))
mail = mail.lower()

true_mail = "ceng113@example.com"
before_at = mail.split("@")[0]
after_at = mail.split("@")[1]
before_at = before_at.replace("." , "")
mail = before_at + "@" + after_at

if true_mail == mail :
    print("Yes")

else :
    print("No")
    
