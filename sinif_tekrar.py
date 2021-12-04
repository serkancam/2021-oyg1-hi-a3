# sinif_yapisi.py
# Eğer bir fonksiyon bir sınıf içinde tanımlanırsa adı metot olur
# __init__ metodu sınftan nesne üretimini gerçekleştiren ve nesnenin ilk özellik değerleri ile başlatılmaısnı sağlayan yapıcı metottur.
# self anahtar kelimesi sınıftan türetilen nesnelerin özelliklerini işaret etmek için kullanılır.
# Sınıf içind eyazılan bir metot o sınıfın özelliklerine sınıf içindne ulaşmak için self anahta kelimesini kullanır.
# sınıf tanımlama
class Canli():
    def __init__(self):#yapıcı metot
        self.agirligi=0.0
        self.boyu=0.0
        self.turu="-"
        # print("Bir canlı oluşturuldu.")
    
    def yuru(self,adim_sayisi:int):
        verilen_kilo=adim_sayisi/1000*100/1000
        self.agirligi=self.agirligi-verilen_kilo



c1 = Canli()#Canli sınıfından c1 adında bir nesne türetildi.
c2 = Canli()
c1.agirligi=20.5
print(f"c1 ağırlığı={c1.agirligi}")
print(f"c2 ağırlığı={c2.agirligi}")
c1.yuru(2000)
print(f"c1 ağırlığı={c1.agirligi}")
c2.agirligi=-200


