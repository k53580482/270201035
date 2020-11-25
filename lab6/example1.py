mail = input("Enter your mail : ")
email = "ceng113@example.com"
new_mail = mail


while True :
  if new_mail != email :
    print("False!")
    mail = input("Enter mail again :")
    before_at = mail.split("@")[0]
    after_at = mail.split("@")[1]
    new_mail = before_at.lower().replace("." , "") + "@" + after_at.lower()

  
  else :
    print("True!")
    break