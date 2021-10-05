# 1-10 arası sayıların toplamı
# toplam= 1+2+3+4+5+6+7+8+9+10
ilk=1
son=2000_000_000
toplam=0
# for sayi in range(ilk,son+1):
#     # print(sayi)
#     toplam+=sayi


toplam=son*(son+1)/2
print(toplam)

# 1- formül ile çözüm
# 2- döngü ile(iteratif)
# 3- özyinelemeli