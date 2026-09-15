# Dictionary: anahtar-deger ciftleri ile bir "kayit" temsil eder

siparis = {
    "musteri" : "Ahmet Yilmaz",
    "urun" : "Laptop",
    "adet": 2,
    "fiyat": 15000
}

print(siparis)
print(siparis["musteri"])   # anahtar ile deger cekmek
print(siparis["fiyat"])

# Yeni anahtar eklemek

siparis["toplam"] = siparis["adet"] * siparis["fiyat"]
print(siparis)

# Birden fazla siparis = dictionary'lerin listesi (tipik bir "veri tablosu" boyle temsil edilir)

siparisler = [
    {"musteri":"Ahmet", "urun": "Laptop", "adet": 1, "fiyat": 15000},
    {"musteri": "Ayse", "urun": "Telefon", "adet": 2, "fiyat": 8000},
    {"musteri": "Mehmet", "urun": "Mouse", "adet": 3, "fiyat": 150},
]

for kayit in siparisler:
    toplam = kayit["adet"] * kayit["fiyat"]
    print(f"{kayit["musteri"]} ->  Toplam: {toplam} TL")