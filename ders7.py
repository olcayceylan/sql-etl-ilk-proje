import psycopg2

# 1. ADIM: Veritabanina BAGLANTI kurmak
# Bunu telefon numarasi cevirmek gibi dusun: hangi adrese, hangi sifreyle baglanacagini soyluyoruz

baglanti = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="postgres",
    user="postgres",
    password="129854"
)

# 2. ADIM: bir "cursor" olustur - bu, veritabanina komut gondermemizi saglayan arac
# Cursor'u "veritabaniyla konusmak icin kullandigimiz mikrofon" gibi dusunebilirsin

cursor =baglanti.cursor()

# 3. ADIM: SQL komutu calistir

cursor.execute("SELECT musteri_adi, toplam_tutar FROM satislar LIMIT 5;")

# 4. ADIM: sonucu Python'a geri CEK

sonuclar=cursor.fetchall()

print("Veritabanindan Gelen Sonuc:")
for satir in sonuclar:
    print(satir)

# 5. ADIM: baglantiyi KAPAT (kapiyi acik birakmamak gibi, kaynaklari bosa harcamamak icin onemli)

cursor.close()
baglanti.close()

print("Baglanti Kapatildi")