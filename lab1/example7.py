name = input("What is your name ? : ")
car_price = int(input("What is your car's price ? : ")) 
discount = float(input("What is your discount for car ? : "))

total_car_price = (car_price - (car_price * discount))

print("You should pay" , total_car_price , name , "!")