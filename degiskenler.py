mustafa=150
keyfi=350
ve_kahyasi=400

# mustafa keyfi ve kahyası paralarını eşit biçimde paylaşırşarsa
# her birinin kaç parası olur.
hbp=(mustafa+keyfi+ve_kahyasi)/3
print(f"ortalama hbp={hbp}")

# mustsafa tanesi 13 tl olan defterlerden en fazla kaç adet alabilir. 
# geriye kaç parası kalır.

fiyat=13
adet=mustafa//fiyat
kalan=mustafa-adet*fiyat

print(f"Mustafa tanesi {fiyat} tl olan defterlerden. {adet} adet alabilir ve geriye {kalan} tl'si kalır.")