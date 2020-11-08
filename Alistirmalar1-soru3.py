def sirala(liste):
    for i in range(len(liste)):
        for j in range(i+1,len(liste)):
            if liste[j] < liste[i]:
                a = liste[i]
                liste[i] = liste[j]
                liste[j]= a
        i += 1
    print("Listemizin sıralanmış hali",liste)


sirala([3,6,4,1,10,12,-1,2,-20])

                
                
                
