parker_hizi=150
ekvator_yaricapi=6378
kutup_yaricapi=6357
pi=3.14
dakika_sn=60
# cevre=2xpixyaricap
ekvator_cevresi=2*pi*ekvator_yaricapi
kutup_cevresi=2*pi*kutup_yaricapi

parker_ekvator_sn=ekvator_cevresi/parker_hizi
parker_kutup_sn=kutup_cevresi/parker_hizi
print(f"parker uzay aracı ekvator çevresini {parker_ekvator_sn} saniyede dolaşır.")
print(f"parker uzay aracı kutup çevresini {parker_kutup_sn} saniyede dolaşır.")

ekvator_dk=int(parker_ekvator_sn//dakika_sn)
ekvator_sn=parker_ekvator_sn%dakika_sn

kutup_dk=int(parker_kutup_sn//dakika_sn)
kutup_sn=parker_kutup_sn%dakika_sn
print(f"parker uzay aracı kutup çevresini {kutup_dk} dakikak {kutup_sn} saniyede dolaşır.")
print(f"parker uzay aracı ekvator çevresini {ekvator_dk} dakikak {ekvator_sn} saniyede dolaşır.")