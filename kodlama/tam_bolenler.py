# kullanıcının girdiği sayının tam bölenlerini ekrana yazdıran programı yazınız.
# 15 --> 1 3 5 15
# 18 --> 1 2 3 6 9 18
# 7 --> 1 7
#62 --> 1 2 31 62
#60 --> 1 2 3 4 5 6 10 12 15 20 30 60

sayi = int(input("sayı giriniz:"))
for i in range(1,sayi+1):
    if sayi%i==0:
        print(i)
    