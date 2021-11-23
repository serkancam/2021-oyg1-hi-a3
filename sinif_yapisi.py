# sinif_yapisi.py
# Eğer bir fonksiyon bir sınıf içinde tanımlanırsa adı metot olur
# __init__ metodu sınftan nesne üretimini gerçekleştiren ve nesnenin ilk özellik değerleri ile başlatılmaısnı sağlayan yapıcı metottur.
# self anahtar kelimesi sınıftan türetilen nesnelerin özelliklerini işaret etmek için kullanılır.
# Sınıf içind eyazılan bir metot o sınıfın özelliklerine sınıf içindne ulaşmak için self anahta kelimesini kullanır.
#sınıf tanımlama
class Insan():
    def __init__(self):#yapıcı metot
        self.ad="-"
        self.soyad="-"
        self.kilo=0.0
        self.boy=0.0
        self.yas=0
        print("yapıcı çalıştı.")


# nesneler-türetmeler

insan1=Insan()#yapıcı metot çalıştı
insan2=Insan()
insan1.ad="mehmet"
insan1.soyad="gül"
insan1.yas=35
insan1.boy=1.74
insan1.kilo=78.0
print(insan1.ad,insan1.soyad,insan1.yas,insan1.boy,insan1.kilo)
print()