def MaximumPathSumII():
    file1 = open("/home/hanpeng/Downloads/p067_triangle.txt")
    list_tri = []

    for i in file1:
        list_tri.append(list(map(int, i.split())))
    
    list_tri = list_tri[::-1]
    ### update binary node sum
    
    for i1, row in enumerate(list_tri[1:]):
        i1+=1
        for i2, node in enumerate(row):
            list_tri[i1][i2] = max(node+list_tri[i1-1][i2],(node+list_tri[i1-1][i2+1]))
    
    return (list_tri[-1][0])
    
    
total = MaximumPathSumI()
print(total)