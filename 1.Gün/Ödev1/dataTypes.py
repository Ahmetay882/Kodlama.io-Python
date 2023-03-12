# VERİ TİPLERİ

# 1.Sayısal Veri Tipleri
    #integer (int) -> Tam sayıları tutan veri tipidir.
    #float -> Ondalık sayıları tutan veri tipidir.
    #complex -> karmaşık sayıları (j) tutan veri tipidir.
sayi1 = 5
print(type(sayi1)) # int

sayi2 = 5.6789
print(type(sayi2)) # float

sayi3 = 1j
print(type(sayi3)) # complex


# Boolean (bool) Veri Tipi -> True/False. Dikkat 'T ve F' büyük harf olmak zorunda.
x = True
y = False
print(type(x)) # bool
print(type(y)) # bool


# String (str) Veri Tipi -> Karakterleri içeren veri tipidir.
metin = "Merhaba Dünya"
print(type(metin)) # str


# Liste (list) Veri Tipi -> Birden fazla elemanı bir arada tutmamızı sağlayan veri tipidir. Python da bu elemanların aynı tipde olma
# zorunluluğu yoktur farklı tiplerde de olabilir.
liste1 = ["Merhaba", "Ahmet", "Halit"]
liste2 = ["Selam", 18, 19.6, 6j]
print(type(liste1)) # list
print(type(liste2)) # list

# Dictionary (dict) Veri Tipi -> Verileri key-value çiftleri şeklinde depolamak ve yönetmek için kullanılan bir veri tipidir.
dict1 = {
    "model" : "TOGG",
    "yil" : "2023"
    }
print(dict1) # {'model': 'TOGG', 'yil': '2023'}
print(dict1["model"]) # TOGG
print(dict1["yil"]) #2023
print(type(dict1)) # dict


# Kümeler (set) Veri Tipi -> Birden fazla farklı tipteki veri türlerini bir arada barındırabilen veri tipidir. 
# Kümelerde eklediğimiz elemandan sadece 1 tane ekleyebiliriz. Kümelerde listeler gibi add, remove, pop gibi metodları bulunmaktadır. 
# Ve bir veri ekleyip silmek istediğimiz zaman bu metodlar aracılığı ile yapmak zorundayız çünkü kümeler indexlenemeyen bir veri tipidir.
kume = {"Python", 'p', 8} 
print(kume) # {8, 'Python', 'p'}
kume2 = {"Python", 'p', 8, "Python"} 
print(kume2) # {8, 'Python', 'p'}
print(type(kume)) # set
print(type(kume2)) # set

# Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
    # Sitedeki kurslar, eğitmenler-> list
kurslar = ["Java", "C#", "Python", "JavaScript", ".NET"]
egitmenler = ["Engin Demiroğ", "Halit Enes Kalaycı"]

    # Sitedeki kursların ve ödevlerin tamamlama yüzdesi -> int 
odevTamamlamaYuzdesi = 50
kursTamamlamaYuzdesi = 25

# Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
    #1.şart bloğu giriş yapma kısmı
kullaniciAdi = "ahmetay"
sifre = "12345"

if kullaniciAdi == "ahmetay" and sifre == "12345":
    print("Giris Basarili")
elif kullaniciAdi != "ahmetay" or sifre != "12345":
    print("Kullanici adi ve sifre hatali")