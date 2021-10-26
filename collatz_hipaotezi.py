# bir sayı alıp çift sayı ise yarısını, tek sayı ise 3 kataının 1 fazlasaını alırsanız
# ve bu işlemi sürekli tekrar edrseniz mutlaka sayı 1'e döner
# sayi= 10 5 16 8 4 2 1
# sayi= 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# sayi= 18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# kullanıcının girdiği sayının collatz hipotezine göre 1'kadar dönmes,ini sağlayan kodu
# şartlı döngü ile yaznız.
# sayi%2==0 ise sayı çift değilse sayı tek
sayi=int(input("Sayı giriniz:"))
adim=1
while sayi!=1:#sayı bir olana kadar veya sayı 1 'den farklı olduğu sürece
    if sayi%2==0:
        sayi=sayi//2
    else:
        sayi=sayi*3+1
    print(f"{adim}. adım değeri={sayi}")
    adim+=1    