book_price = 24.95
dicount = 0.4
first_shipping = 3
other_shipping = 0.75
copies = 60

total_book_price = (book_price * copies) * (1 - dicount)
total_shipping_price = (first_shipping + (other_shipping * (copies - 1)))

total_price = total_book_price + total_shipping_price

print(total_price)