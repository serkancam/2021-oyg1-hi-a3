#******tanımlamalar*******
# 1- parametre almayan geriye değer döndürmeyen
def merhaba():
    print("merhaba")

def merhaba2():
    for i in range(4):
        print("selamlar")

# 2- parametre alan geriye değer döndürmeyen
def merhaba3(adet):
    for i in range(adet):
        print("sa")

def topla(sayi1,sayi2):
    t=sayi1+sayi2
    print(t)
# 3- parametre almayan geriye değer döndüren
def pi_sayisi():
    return 3.14
# 4- parametre alan geriye değer döndüren
def kare_farki(s1,s2):
    fark=s1**2-s2**2
    return fark


#******çağrılar*********
merhaba()
merhaba()
merhaba2()
merhaba3(5)
topla(3,5)
deger=pi_sayisi()
print(deger)
a1=float(input("sayı 1'i giriniz:"))
a2=float(input("sayı 2'yi giriniz:"))
hesapla=kare_farki(a1,a2)
print(hesapla)