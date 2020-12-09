numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
numbers1 = set(numbers1)
numbers2 = set(numbers2)

uni = list(numbers1) + list(numbers2)
uni = set(uni)
intr = []

for i1 in numbers2:
    if i1 in numbers1 :
        intr.append(i1)

intr = set(intr)
print("The intersection of these sets ->", intr)
print("The union of these sets ->", uni)

