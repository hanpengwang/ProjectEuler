def Fibonacci1000(NumDigits):
    FibList = [1,1]
    Count = 1 
    num = 0
    while num<NumDigits: 
        num = sum(FibList[Count-1:Count+1])
        FibList.append(num)
        Count += 1 

    print(Count+1)
    
print(Fibonacci1000(1000))
