#Liste: birden fazla degeri tek bir kutuda tutmak
urunler = ["Laptop","Telefon", "Kulaklik","Klavye"]

print(urunler)          # tum listeyi yazdirir
print(urunler[0])       # ilk eleman (Python'da sayma 0'dan baslar!)
print(urunler[2])       # ucuncu eleman
print(len(urunler))     # listede kac eleman var

# for dongusu: listedeki HER elemani tek tek gezip islem yapmak icin

for urun in urunler:
    print(f"Urun: {urun}")

# ETL senaryosu: her urune bir KDV hesaplama islemi uygulayalim

fiyatlar = [1000, 500, 200, 150]

for fiyat in fiyatlar:
    kdv_dahil = fiyat * 1.20
    print(f"KDV haric: {fiyat} TL -> KDV dahil: {kdv_dahil} TL")
