def printN(num):
    if num==1:
        print(num)
    elif(num>1):
        printN(num-1)
        print(num)

printN(-10)