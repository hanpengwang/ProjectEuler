def Freefarea(n):
    Collect = 0
    import itertools as it
    S = ['a','e','f','r']
    Sn = ['free','fare','area','reef']
    C = it.product(S, repeat = n)
    for i in C:
        Word = ''.join(i)
        FreeCount = 0
        FareCount = 0
        AreaCount = 0
        ReefCount = 0
        for i2 in range(len(Word)):
            SubWord = Word[i2:i2+4]
            if SubWord == Sn[0]:
                FreeCount+=1
            elif SubWord == Sn[1]:
                FareCount+=1
            elif SubWord == Sn[2]:
                AreaCount+=1
            elif SubWord == Sn[3]:
                ReefCount+=1

        if FreeCount == 1 and FareCount == 1 and AreaCount == 1 and ReefCount == 1:
            Collect+=1

    return(Collect)

Freefarea(30)
