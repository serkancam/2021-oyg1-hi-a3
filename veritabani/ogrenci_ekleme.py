import sqlite3 as sql

try:
    okul_no = int(input("okul no:"))
    ad=input("ad:")
    soyad=input("soyad:")
    sinif=int(input("sınıf:"))
    sube=input("şube:")
    #1- bağlantı
    vt=sql.connect("/home/serkan/Belgeler/2021-oyg1-hi-a3/veritabani/okul.db")
    #2- sql cümleciği
    ekleme_sql="insert into ogrenci values(?,?,?,?,?)"
    #3- alınan bilgileri liste yap
    degerler=[okul_no,ad,soyad,sinif,sube]
    #4- cursor(imleç) oluştur.
    imlec = vt.cursor()
    #5- sql cümleciği ile  değerleri kullanarak cursor üzerinden execute etmek
    imlec.execute(ekleme_sql,degerler)
    vt.commit()
    print(imlec)
except:
    print("hatalı işlem")
finally:
    #7-8 cursor ve bağlantıyı kapat
    if imlec:
        imlec.close()
    if vt:
        vt.close()