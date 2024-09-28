def printNumber(n):
    itr = 0
    print("The number user entered: ", n)
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
            itr+=1
        print("")
    print("The iterations done by this code: ", itr)
        
printNumber(5)