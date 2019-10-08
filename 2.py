def EvenFibonacc(Max):
    collect = [2,]
    NumList = [1,2]
    num = 0
    while num <= Max:
        
        num = sum(NumList[-2: ])
        NumList.append(num)
        if num%2 == 0:
            collect.append(num)
    if collect[-1] > Max:
        collect.pop()
    return (sum(collect))
EvenFibonacc(4*10**6)
