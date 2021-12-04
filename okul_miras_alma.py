class Kisi():#ata sınıf, parent class,super
    def __init__(self,adi:str,soyadi:str):
        self.adi=adi
        self.soyadi=soyadi
        self.dogum_tarihi="01.01.1900"

class Ogrenci(Kisi):
    def __init__(self,ad,soyad,sinifi:int,subesi:str,numara:int):
        super().__init__(ad,soyad)
        self.sinifi=sinifi
        self.subesi=subesi
        self.numarasi=numara

class Ogretmen(Kisi):
    def __init__(self, adi: str, soyadi: str,brans:str,kidem:int):
        super().__init__(adi, soyadi)
        self.brans=brans
        self.kidem=kidem


k1=Kisi("hasan","can")
o1=Ogrenci("leyla","kut",9,"A",58)
# o1.adi="leyla"
# o1.soyadi="mutlak"
o1.dogum_tarihi="12.12.2010"
ogt1=Ogretmen("ayşe","kan")
print(o1.adi,o1.soyadi)
