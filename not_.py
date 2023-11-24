def ortalama():
    print("╔═════════════════════════════════╗")
    print("║     TAKDİR TEŞEKKÜR HESAPLAMA   ║")
    print("╚═════════════════════════════════╝")
    ders_sayisi=int(input("ders sayısını gir:"))
    s=0
    for x in range(ders_sayisi):
        ders=int(input(x+1,".Dersin ortalaması:"))
        s=s+ders
    s=s/ders_sayisi
    if(s>=85):
        print("*****TAKDİR*******")
    elif(s>=70):
        print("**TEŞEKKÜR**")
    else:
        print("CANININ SAĞLIĞI")
