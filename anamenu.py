import hesapmakinesi
import sekilcizdirme
import takvim
import ritmik_sayma
import oyunlar
import not_
import çarpım_tablosu
import bmi
import döviz
import termometre
def Anamenu():
    print("╔═══════════════════════╗")  #şekli oluşturmak için alt tuşuna basılı tut ascii karşılığına bas
    print("║   PYTHON ÇALIŞMALARI  ║")
    print("║ 1-HESAP MAKİNESİ      ║")
    print("║ 2-OYUNLAR             ║")
    print("║ 3-ŞEKİL ÇİZDİRME      ║")
    print("║ 4-TAKVİM              ║")
    print("║ 5-RİTMİK SAYMA        ║")
    print("║ 6-NOT HESAPLAMA       ║")
    print("║ 7-ÇARPIM TABLOSU      ║")
    print("║ 8-BMI HESAPLAMA       ║")
    print("║ 9-DÖVİZ UYGULAMASI    ║")
    print("║ 10-SICAKLIK ÇEVİRME   ║")
    print("║ 11-ÇIKIŞ (e)          ║")
    print("║    Seçimini yap       ║")
    print("╚═══════════════════════╝")
    secim = input("Seçiminiz:")
    if (secim == '1'):
        hesapmakinesi.hesapmakinesi()
        Anamenu()
    if (secim == '2'):
        oyunlar.oyun()
        Anamenu()
    if(secim == '3'):
        sekilcizdirme.ana()
        Anamenu()
    if(secim=='4'):
        takvim.takvim()
        Anamenu()
    if(secim=='5'):
          ritmik_sayma.ritmik_sayma()
          Anamenu()
    if(secim=='6'):
        not_.ortalama()
    if(secim=='7'):
        çarpım_tablosu.carpim_tablosu()
    if(secim=='8'):
        bmi.bmi()
    if(secim=='9'):
        döviz.doviz()
    if(secim=='10'):
        termometre.termometre()
    if (secim == '11' or secim == 'e' or secim == 'E'):
        print("Çıkış yapılıyor...")

