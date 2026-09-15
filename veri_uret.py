import pandas as pd
import numpy as np
import random

# Rastgele ama tekrar üretilebilir veri için sabit tohum
np.random.seed(42)
random.seed(42)

# 500 satırlık sahte satış verisi üretelim
n = 500

musteri_adlari = ["Ahmet Yilmaz", "Ayse Kaya", "Mehmet Demir", "Fatma Sahin", 
                   "Ali Celik", "Zeynep Arslan", "Mustafa Yildiz", "Elif Aydin"]

urunler = ["Laptop", "Telefon", "Kulaklik", "Klavye", "Mouse", "Monitor", "Tablet", "Sarj Aleti"]

kategoriler = {"Laptop": "Elektronik", "Telefon": "Elektronik", "Kulaklik": "Aksesuar",
               "Klavye": "Aksesuar", "Mouse": "Aksesuar", "Monitor": "Elektronik",
               "Tablet": "Elektronik", "Sarj Aleti": "Aksesuar"}

veri = []
for i in range(n):
    urun = random.choice(urunler)
    fiyat = round(random.uniform(50, 2000), 2)
    
    # Kasıtlı olarak bazı satırları "kirli" yapalım (gerçek hayatta böyle olur)
    if random.random() < 0.05:  # %5 ihtimalle fiyat eksik
        fiyat = None
    if random.random() < 0.03:  # %3 ihtimalle negatif miktar (hatali veri)
        adet = -1
    else:
        adet = random.randint(1, 5)
    
    musteri = random.choice(musteri_adlari)
    if random.random() < 0.04:  # %4 ihtimalle musteri adi bos
        musteri = None
    
    tarih = pd.Timestamp("2025-01-01") + pd.Timedelta(days=random.randint(0, 300))
    
    veri.append({
        "siparis_id": i + 1,
        "musteri_adi": musteri,
        "urun": urun,
        "kategori": kategoriler[urun],
        "adet": adet,
        "birim_fiyat": fiyat,
        "tarih": tarih
    })

df = pd.DataFrame(veri)

# Bazı tam duplike satırlar ekleyelim (gerçek veride sık olur)
duplikeler = df.sample(10, random_state=1)
df = pd.concat([df, duplikeler], ignore_index=True)

df.to_csv("satislar_ham.csv", index=False, encoding="utf-8-sig")
print("Veri seti olusturuldu: satislar_ham.csv")
print(f"Toplam satir sayisi: {len(df)}")