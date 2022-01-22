# 366 kişilik bir okul gezisi için her biri 45 kişi taşıyan otobüsler 
# kiralancaktır. Bu gezi için en az kaç otobüs kiralanması gerekir.
# fakat bu 366 kişide geziye kesin katılacktır
kisi=360
otobus_kapasitesi=45
otobus_adeti=kisi//otobus_kapasitesi
kalan= kisi%otobus_kapasitesi

if kalan>0:
    otobus_adeti+=1

print(f"{kisi} kişiyi geziye götürmek için en az {otobus_adeti} kadar otobüs kiralanması gerekir.")