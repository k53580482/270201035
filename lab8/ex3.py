import random

list1 = []
list2 = []

def get_rand_list(b = 0, e = 10, N = 5):
    for i in range(N):
        list1.append(random.randint(b, e))
    for i in range(N):
        list2.append(random.randint(b, e))

get_rand_list()
print(list1)
print(list2)

overlap = []
def get_overlap(list1, list2):
    for i in list1:
        if i in list2:
            overlap.append(i)
        else :
            pass

get_overlap(list1, list2)
print("The overlap of these two lists : ", overlap)