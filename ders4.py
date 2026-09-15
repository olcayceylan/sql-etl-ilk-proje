import pandas as pd

# DataFrame: tipki bir Excel tablosu gibi dusun (satirlar ve sutunlar)

veri = {
    "musteri": ["Ahmet", "Ayse", "Mehmet"],
    "urun": ["Laptop", "Telefon", "Mouse"],
    "adet": [1, 2, 3],
    "fiyat": [15000, 8000, 150]
}

df=pd.DataFrame(veri)

print(df)
print("---")
print(df["musteri"])    # tek bir sutunu secmek 
print("---")
print(df.head())    # ilk 5 satiri gosterir (bizde 3 satir oldugu icin hepsi gorunur)
print("---")
print(df.describe())    # sayisal sutunlar icin ozet istatistik
print("---")

# Yeni bir sutun turetmek (ETL'de "transform" adimi tam olarak budur)

df["toplam"] = df["adet"] * df["fiyat"]
print(df)