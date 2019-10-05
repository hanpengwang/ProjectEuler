def Divide3or5(num):
    collect = []
    for i in range(num)[1:]:
        if i%3 == 0 or i%5 == 0:
            collect.append(i)
    return sum(collect)
    
print(Divide3or5(1000))
