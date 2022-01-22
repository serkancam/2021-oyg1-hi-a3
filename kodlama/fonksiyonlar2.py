# aldığı parametreler ile bir dikdörtgenin çevresini hesaplayıp hesapladığı değeri geri döndüren bir fonksion yazınız

import turtle as t


def dikdortgen_cevresi(kk,uk):
    cevre=(kk+uk)*2
    return cevre

def delta(a:float,b:float,c:float)->float:
    d=b**2-(4*a*c)
    return d

def ortalama(s1:float,s2:float,s3:float)->float:
    ort=(s1+s2+s3)/3
    return ort


delta(3,6,8)

t.forward()
t.position()
t.color()
