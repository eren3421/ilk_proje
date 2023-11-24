def yazitura():
    import random
    yt=random.randint(1,2)
    tahmin=input("YAZI TURA?")
    if yt==1:
        print("YAZI")
    else:
        print("TURA")
    if yt==1:
        atilan="YAZI"
    else:
        atilan="TURA"
    if tahmin==atilan:
        print("KAZANDIN")
    else:
        print("KAYBETTİN")
    secim=input("DEVAM ETMEK İSTİYOR MUSUN")
    if(secim=='e' or seim=='E'):
        yazitura()
