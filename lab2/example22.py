x = input("How many Fibonacci numbers do you want to use : ")
a = 1
b = 1

print(a)
print(b)

for i in range(1, x-1): 
  (a,b) = (a + b , a + 2*b) 

print(a)
print(b)
