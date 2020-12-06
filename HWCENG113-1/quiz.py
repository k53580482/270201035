mail_dict = {
  "alice" : "alice@example.com" ,
  "bob" : "bob@example.com" , 
  }

  while True : 
    a = input("Enter your mail : ")
    mail_dict = list(mail_dict)
    mail_dict.append(a)
print(mail_dict)