# fonksiyona_parametre_yollama.py
# tanımlama
def yamuk_cevresi(a, b, c, d):
    cevre = a+b+c+d
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    print(f"d={d}")
    return cevre


a1=5
b1=6
c1=10
d1=8
## parametre gönderme yöntemleri##
# 1- Pozisyona dayalı parametre gönderme
yc1=yamuk_cevresi(d1,b1,c1,a1)
print(yc1)
# 2- İsme dayalı parametre gönderme 
yc2 = yamuk_cevresi(b=8,c=10,d=22,a=4)
print(yc2)
# 3- karışık kullanım
yc3 = yamuk_cevresi(5,8,d=10,c=11)# soldan ilk isme dayalı parametre gönderiminden sonra her parametre isme dayalı gitmeli
print(yc3)