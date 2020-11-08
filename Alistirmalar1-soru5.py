def futbolcular():
    liste = []
    for i in range(5):
        isim = input("İsim:")
        soyisim = input("Soy İsim:")
        takim = input("Takımı:")
        if takim == "Barcelona":
            liste.append([isim,soyisim,takim])
        
    print(liste)


futbolcular()
