def sleep(t):
    if t == 0:
        return "Alert"
    else :
        return  "waits for " + str(t) + " seconds\n" + sleep(t-1)

print(sleep(6))