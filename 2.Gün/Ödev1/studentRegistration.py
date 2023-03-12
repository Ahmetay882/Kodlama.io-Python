# Ödev İsterleri:
    # Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
    # Bu öğrenci kayıt sistemine;
        # Aldığı isim soy isim ile listeye öğrenci ekleyen    
        # Aldığı isim soy isim ile eşleşen değeri listeden kaldıran 
        # Listeye birden fazla öğrenci eklemeyi mümkün kılan  
        # Listedeki tüm öğrencileri tek tek ekrana yazdıran 
        # Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
        # Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız) 
        # fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz. 
    # Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


# Boş bir liste oluşturdum.
students = list()

# Listeye eklemek için öğrencinin adını ve soyadını aldım.
def nameSurname():
    name = input("Adinizi giriniz: ")
    surname = input("Soyadinizi giriniz: ")
    
    nameSurname = name + surname
    
    print("Öğrenci başarili bir şekilde eklendi.")
    print(f"Girmiş olduğunuz öğrencinin ad ve soyadi: {nameSurname}")
    
    return nameSurname

# nameSurname fonksiyonu ile aldığım öğrencileri oluşturduğum boş listeye ekledim.
def studentAdd(student):
    while True:
        students.append(student)
        
        exit = int(input("Öğrenci eklemek icin 1'e basiniz. Diğer işlemler için baska bir sayiya basiniz: "))
        if (exit == 1):
            student = nameSurname()
        else:
            break
    
    return students

# Öğrenci silme işlemini yaptığım fonksiyon.
def deleteMethod():
    result = input("Silmek istediğiniz öğrencinin adini ve soyadini giriniz: ")
    students.remove(result)
    
    print("Silmek istediğiniz öğrenci başarili bir şekilde silindi. Kalan öğrencilerin listesi: ")
    
    studentPrint()

# Öğrenci silme işlemini döngüye soktuğum fonksiyon.
def studentDelete():
    while True:
        deleteMethod()
        
        delete = int(input("Başka bir öğrenci daha silmek icin 1'e basiniz. Diger işlemler için başka bir sayiya basiniz: "))
        if (delete == 1):
            deleteMethod()
        else:
            break
    
    return students

# Öğrencileri tek tek yazdırdığım fonksiyon.
def studentPrint():
    print("Kurumumuzda bulunan öğrenci: ")
    
    for i in range(len(students)):
        print(students[i])

# Öğrencilerin listedeki index'ini numarası olmasını sağladığım fonksiyon. 
def studentNo():
    print("Kurumumuzda bulunan öğrenci ve numaralari: ")
    
    for i in range(len(students)):
        print(f"Student: {students[i]} Number: {i}")

def main():
    print("**********     Öğrenci Kayit Sistemimize Hoşgeldiniz !!     **********")
    print("\n")
    
    student = nameSurname()
    print("\n")
    
    print("Uygulamamizda yapabileceğiniz işlemler: ")
    options = ["1-Öğrenci Ekleme", "2-Öğrenci Silme", "3-Öğrenci İsimlerini Listeleme", "4-Öğrenci İsimlerini ve Numaralarini Listeleme", "5-Çikiş"]
    
    while True:
        for i in range(len(options)):
            print(options[i])
        
        islem = int(input("Yapmak istediginiz islemi seciniz: "))
        if (islem == 1):
            studentAdd(student)
        elif (islem == 2):
            studentDelete()
        elif (islem == 3):
            studentPrint()
        elif (islem == 4):
            studentNo()
        elif (islem == 5):
            break
        else:
            print("Geçersiz işlem. Tekrar seçim yapiniz: ")

main()