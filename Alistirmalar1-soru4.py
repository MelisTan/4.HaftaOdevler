def TekCift(liste):
    tek = []
    cift = []
    for i in liste:
        if i % 2 == 1:
            tek.append(i)
        else:
            cift.append(i)

    print([cift,tek])
    
TekCift([1,2,3,4,5,6,7,8,9,10])

