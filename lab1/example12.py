age = int(input("Your age : "))
bprice = 3
discount_rate = 0.5

if age < 6 or age > 60 :
    price = 0


elif age > 6 and age < 18 :
    price = bprice * (1 - discount_rate)

else :
    price = bprice

print(price)