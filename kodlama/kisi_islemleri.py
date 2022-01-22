from kisi import Kisi
while True:
    islem = int(input("(0-okuma,1-ekleme,2-yaş ortalaması,3-çıkış) işlem seç:"))
    if islem==0:
        print("okuma")
        dosya=open("kisiler.txt","r",encoding="utf-8")
        for satir in dosya:
            print(satir,end="")
        dosya.close()
    elif islem==1:
        print("ekleme")
        while True:
            ad=input("ad giriniz:")
            soyad=input("soyad giriniz:")
            try:
                yas=int(input("yaş giriniz:"))
            except:
                print("yaş değeri tam sayı olmalıdır.")
                continue
            if len(ad)<2 or len(soyad)<2 or yas<0:
                print("ad soyad değerien az 2 karakterli yaş değeri 0'dan büyük olmalı")
                continue
            kisi1 = Kisi(ad,soyad,yas)
            kisi1.kayit("kisiler.txt")
            break
    elif islem==2:
        print("yaş ortalaması")
        dosya = open("kisiler.txt","r",encoding="utf-8")
        ortalama=0
        adet=0
        for s in dosya:
            yas = int( s.split(",")[2].strip())
            ortalama=ortalama+yas#ortalama+=yas
            adet=adet+1#adet+=1
        ortalama=ortalama/adet
        print(f"yaş ortalaması = {ortalama}")
    elif islem==3:
        print("çıkış.")
        break
    else:
        print("hatalı seçim.")