def doviz():
    print("╔═════════════════════════╗")
    print("║       $$$$$$$           ║")
    print("║    DÖVİZ UYGULAMASI     ║")
    print("║   ££££££££ TL  €€€€€€€€ ║")
    print("╚═════════════════════════╝")
    print("TL için T USD için D EURO ")
    print("STERLİN için S:")
    secim=input("Elinizdeki para birimini girin:")
    miktar=int(input("Para miktarını girin:"))
    secim2=input("Çevirmek istediğiniz birimi girin")
    if(secim=='T' and secim2=='D'):
        print(miktar,secim,"=",(miktar/28.80),secim2)
    elif(secim=='T' and secim2=='E'):
        print(miktar,secim,"=",(miktar/31.52),secim2)
    elif(secim=='T' and secim2=='S'):
        print(miktar,secim,"=",(miktar/36.10),secim2)
    elif(secim=='D' and secim2=='T'):
        print(miktar,secim,"=",(miktar*28.80),secim2)
    elif(secim=='D' and secim2=='E'):
        print(miktar,secim,"=",(miktar/1.09),secim2)
    elif(secim=='D' and secim2=='S'):
        print(miktar,secim,"=",(miktar/1.25),secim2)
    elif(secim=='E' and secim2=='T'):
        print(miktar,secim,"=",(miktar*31.52),secim2)
    elif(secim=='E' and secim2=='D'):
        print(miktar,secim,"=",(miktar*1.09),secim2) 
    elif(secim=='E' and secim2=='S'):
        print(miktar,secim,"=",(miktar/1.15),secim2)
    elif(secim=='S' and secim2=='T'):
        print(miktar,secim,"=",(miktar*36.10),secim2)
    elif(secim=='S' and secim2=='D'):
        print(miktar,secim,"=",(miktar*1.25),secim2)
    elif(secim=='S' and secim2=='E'):
        print(miktar,secim,"=",(miktar*1.15),secim2)