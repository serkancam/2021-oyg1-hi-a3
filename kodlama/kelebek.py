# sayi=3
# *
# ** 
# ***
# sayi=6
# *
# **
# ***
# ****
# *****
# ******


# while t<=sayi
# while t<=sayi:
#     k=1
#     while k<=t:
#         print("*",end="")
#         k=k+1
#     print()
#     t=t+1:
#     k=1
#     while k<=t:
#         print("*",end="")
#         k=k+1
#     print()
#     t=t+1


# sayi=4
# *
# **
# ***
# ****
# ***
# **
# *
sayi=int(input("sayı giriniz:"))
t=1  # 2 3 4 ... sayi
while t<=sayi:
    print(t*"*")
    t=t+1
t=t-2
while t>=1:
    print(t*"*")
    t=t-1