# SQL & ETL İlk Projem

Python ve PostgreSQL kullanarak uçtan uca bir ETL (Extract-Transform-Load) pipeline'ı geliştirdim.

## Ne Yapıyor?

1. **Extract**: Sentetik (kasıtlı kirli) satış verisi üretiliyor (`veri_uret.py`)
2. **Transform**: pandas ile veri temizleniyor — eksik değerler dolduruluyor, duplike satırlar siliniyor, yeni sütunlar türetiliyor
3. **Load**: Temizlenmiş veri psycopg2 ile PostgreSQL veritabanına yükleniyor

## Kullanılan Teknolojiler

- Python (pandas, psycopg2, python-dotenv)
- PostgreSQL
- SQL (GROUP BY, window fonksiyonları, CTE)

## Klasördeki Dosyalar

- `veri_uret.py` — ham/kirli veri üretir
- `temizle_ve_yukle.py` — veriyi temizleyip veritabanına yükler
- `ders1.py` - `ders7.py` — Python ve pandas öğrenirken yazdığım pratik dosyalar

## Örnek SQL Sorguları

Projede window fonksiyonları (RANK, LAG) ve CTE kullanarak aylık gelir trendi ve müşteri sıralaması gibi analizler yaptım.

## Notlar

Veritabanı bağlantı bilgileri güvenlik için `.env` dosyasında tutulmakta ve GitHub'a yüklenmemektedir.