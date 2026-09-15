import pandas as pd

# CSV dosyasini oku

df=pd.read_csv("ornek_veri.csv")
print("Okunan Veri:")
print(df)
print("---")

# Temizleme (bir onceki derste ogrendiklerimiz)

df["fiyat"] = df["fiyat"].fillna(df["fiyat"].mean())
df["musteri"] = df["musteri"].fillna("Bilinmiyor")
df=df.drop_duplicates()

print("Temizlenmis Veri:")
print(df)
print("---")

# Yeni sutun turet

df["toplam"] = df["fiyat"] * df["adet"]
print("Toplam Sutunu Eklenmis:")
print(df)
print("---")

# Temizlenmis veriyi YENI bir CSV dosyasina yaz

df.to_csv("temiz_veri.csv, index=False")
print("temiz_veri.csv dosyasi olusturuldu")