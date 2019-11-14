import numpy as np

def SpiralDiagonals(dim):
    mat = np.zeros([dim,dim])
    if dim % 2 ==0:
        raise Exception("dim should be odd")
    rowMover = dim//2 
    colMover = dim//2
    mat[rowMover,colMover] = 1
    firstNum = 1
    count = 0
    while rowMover!=0 and colMover!=dim-1:
        colMover += 1 
        firstNum += 1
        mat[rowMover,colMover] = firstNum
        for i1 in range(count*2 + 1):
            rowMover += 1
            firstNum += 1
            mat[rowMover,colMover] = firstNum
        for i2 in range(count*2 + 2):
            colMover -= 1
            firstNum += 1
            mat[rowMover,colMover] = firstNum
        for i3 in range(count*2 + 2):
            rowMover -= 1
            firstNum += 1
            mat[rowMover,colMover] = firstNum
        for i4 in range(count*2 + 2):
            colMover += 1
            firstNum += 1
            mat[rowMover,colMover] = firstNum
        
        count += 1
        
    return(mat[:, ::-1].trace() + mat.trace() - 1)
        
        
    
print(SpiralDiagonals(1001))
    
