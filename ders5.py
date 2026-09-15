import pandas as pd
import numpy as np

# None / np.nan = "bu veri eksik/bilinmiyor" anlamina gelir
veri = {
    "musteri": ["Ahmet", "Ayse", None, "Mehmet", "Ahmet"],
    "urun": ["Laptop", "Telefon", "Mouse", "Klavye", "Laptop"],
    "fiyat": [15000, None, 150, 300, 15000]
}

df = pd.DataFrame(veri)
print("ORIJINAL VERI:")
print(df)
print("---")

# Hangi hucrelerde eksik veri var, kontrol edelim
print("Eksik Veri Kontrolu:")
print(df.isnull())
print("---")

# Her sutunda kac eksik deger var

print("Her Sutunda Kaç Eksigi Var:")
print(df.isnull().sum())
print("---")

# 1. YONTEM: eksik verisi olan SATIRI komple sil

temiz_v1 = df.dropna()
print("dropna() Sonrası:")
print(temiz_v1)
print("---")

# 2. YONTEM: eksik veriyi bir deger ile DOLDUR

temiz_v2 =df.copy()
temiz_v2["fiyat"] = temiz_v2["fiyat"].fillna(temiz_v2["fiyat"].mean())
temiz_v2["musteri"] = temiz_v2["musteri"].fillna("Bilinmiyor")
print("fillna() Sonrası:")
print(temiz_v2)
print("---")

# Duplike (tekrar eden) satirlari bulma ve silme

print("Duplike Kontrolu:")
print(df.duplicated())
temiz_v3 = df.drop_duplicates()
print("drop.duplicates() Sonrası:")
print(temiz_v3)

