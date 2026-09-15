# Bir degisken, bir kutu gibidir - icine deger koyarsin

musteri_adi = "Ahmet Yilmaz"
adet = 5
fiyat= 149.99


# print() ile ekrana yazdiririz

print(musteri_adi)
print(adet)
print(fiyat)


# f-string: metin icine degisken gomme yontemi (ETL'de raporlama icin cok kullanilir)

print(f"{musteri_adi} adli musteri {adet} adet urun aldi, birim fiyat {fiyat} TL")


# tip kontrolu

print(type(musteri_adi))
print(type(adet))
print(type(fiyat))

