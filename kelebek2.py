# #sayi=4
# *      *
# **    **
# ***  ***
# ********

sayi=int(input("sayı giriniz:"))
t=1
while t<=sayi:
    bs=(sayi-t)*2
    print(t*"*",bs*" ",t*"*",sep="")
    t=t+1