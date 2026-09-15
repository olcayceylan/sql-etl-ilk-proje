from dotenv import load_dotenv
import os

load_dotenv()


import pandas as pd
import psycopg2
from psycopg2 import sql

# --- 1. ADIM: HAM VERIYI OKU ---
df = pd.read_csv("satislar_ham.csv")
print(f"Ham veri okundu: {len(df)} satir")

# --- 2. ADIM: TEMIZLEME ---

# a) Tam duplike satirlari sil
df = df.drop_duplicates()
print(f"Duplikeler silindikten sonra: {len(df)} satir")

# b) Musteri adi bos olan satirlari sil (bu veride musteri kimligi kritik)
df = df.dropna(subset=["musteri_adi"])
print(f"Musteri adi bos olanlar silindikten sonra: {len(df)} satir")

# c) Fiyati bos olan satirlar icin, o urunun ortalama fiyatiyla doldur
df["birim_fiyat"] = df.groupby("urun")["birim_fiyat"].transform(
    lambda x: x.fillna(x.mean())
)

# d) Negatif adet degerlerini gecersiz kabul edip sil
df = df[df["adet"] > 0]
print(f"Negatif adetler silindikten sonra: {len(df)} satir")

# e) Toplam tutar sutunu ekle (ETL'de turetilmis alan ornegi)
df["toplam_tutar"] = (df["adet"] * df["birim_fiyat"]).round(2)

# f) Tarihi gercek tarih tipine cevir
df["tarih"] = pd.to_datetime(df["tarih"])

print("\nTemizlenmis veri ozeti:")
print(df.info())

# Temizlenmis veriyi de bir CSV olarak sakla (kontrol amacli)
df.to_csv("temiz_veri.csv", index=False, encoding="utf-8-sig")
print("\nTemiz veri kaydedildi: satislar_temiz.csv")

# --- 3. ADIM: POSTGRESQL'E YUKLE ---

BAGLANTI = {
    "host": "localhost",
    "port": "5432",
    "dbname": "postgres",
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD")
}

conn = psycopg2.connect(**BAGLANTI)
cur = conn.cursor()

# Tabloyu olustur (varsa once sil)
cur.execute("DROP TABLE IF EXISTS satislar;")
cur.execute("""
    CREATE TABLE satislar (
        siparis_id INTEGER,
        musteri_adi VARCHAR(100),
        urun VARCHAR(100),
        kategori VARCHAR(50),
        adet INTEGER,
        birim_fiyat NUMERIC(10,2),
        tarih DATE,
        toplam_tutar NUMERIC(10,2)
    );
""")
conn.commit()
print("\nTablo olusturuldu: satislar")

# Veriyi satir satir yukle
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO satislar (siparis_id, musteri_adi, urun, kategori, adet, birim_fiyat, tarih, toplam_tutar)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row["siparis_id"]), row["musteri_adi"], row["urun"], row["kategori"],
        int(row["adet"]), float(row["birim_fiyat"]), row["tarih"].date(), float(row["toplam_tutar"])
    ))

conn.commit()
print(f"{len(df)} satir PostgreSQL'e yuklendi.")

cur.close()
conn.close()