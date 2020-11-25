num_of_items = int(input("Numbers of items :"))

a = []
for i in range(1, num_of_items + 1) :
  li = (input("What is item :"))
  if li not in a :
    a.append(li)
  
a.sort()
print(a[::-1])
