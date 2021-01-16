def binary_to_dec():
    bin = str(int(input("Enter a number(0/1):")))
    len1 = len(bin)
    result = 0
    for i in bin:
        if int(i) == 1 :
            app = 2 ** (len1 - 1)
            result += app
            len1 -= 1
        else :
            len1 -= 1
            pass

    print(result)



def dec_to_binary():
    dec = int(input("Enter a number:"))
    result = int(bin(dec)[2:])
    print(result)

dec_to_binary()