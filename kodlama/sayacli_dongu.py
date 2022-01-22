# programlama dillerinde bir başlangıç ve bitiş değeri arasındaki belirlenenbir değişim
# değeri ile sayan döngüye sayaçlı döngü denir.

# pythonda sayı aralığını range()  komutu oluşturur.
# 1- range(bitis)--> burada başlangıç 0 değişim +1 kabul edilir.
# 2- range(baslangic,bitis)--> burada değişim +1 kabul edilir
# 3- range(baslangic,bitis,degisim)

for i in range(5):#0 1 2 3 4
    print(i)

print(30*"*")

for t in range(5,10):
    print(t)

print(30*"*")

for a in range(10,5):# bu döngü hiç bir zaman çalışmaz.
    print(a)

# 10 dan 0 kadar 0 dahil geriye doğru 2 şer 2 2şer sayan for döngüsünü yazınız.
print(30*"*")
for b in range(10,-1,-2):
    print(b)

print(30*"*")
liste=[3,5,2,7]

for e in liste:
    print(e)
print(30*"*")
ad="serkan merhaba nasılsın?"#karakter dizisi
for harf in ad:
    print(harf)













