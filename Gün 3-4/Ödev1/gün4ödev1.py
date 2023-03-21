"""
# ----- HTML -----
HTML -> HyperText Markup Language (Hiper Metin İşaretleme Dili)
HTML, bir web sayfasının içeriğini (paragraflar, başlıklar, bağlantılar) yapılandırmak için kullanılan basit bir biçimlendirme dilidir.
Son ve en güncel sürümü HTML5 'dir.
"""

# -------------------------------------------------------------------------------------------------------------------------------------

"""
# ----- HTML LOCATORS -----
Bir yer bulucu, test uzmanlarının üzerinde işlem yapılacak bir HTML DOM öğesi seçmesini sağlar.
Herhangi bir websitesine girdiğimizde yapabileceğimiz belli başlı bazi işlemler vardır. Input girmek, kayıt olmak, belirli alanlara 
tıklamak gibi işlemler yapabiliyoruz. Bu işlemlerin doğru çalışması için girilen sitenin doğru ve istenilen şekilde çalışması için 
sitenin halka açılmadan önce ve halka açıldıktan sonra da devam etmek üzere bazı test işlemleri yapılır. Örneğin kullanıcı giriş 
yaparken geçerli karakterler girdi mi girmedi mi veya kullanıcının tıkladığı alanlarda istenilen çıktılar verildi mi gibi işlemleri 
kontrol etmek lazım. Bu tarz işlemleri manuel yapmak çok zaman alır. Selenium ile bu tarz işlemler çok daha kısa sürede yapabilmekteyiz.
Ancak bir alanı test edebilmemiz için önce o alana/elemente ulaşabilmemiz lazım.Site üzerindeki bir elemente örneğin giriş butonuna 
selenium ile tıklama işlemi yaptırmak istediğimizde bu işlemi locator’lar(konumlandırıcılar) aracılığıyla yaparız.
Locators(Konumlandırıcı), Selenium IDE'ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur. 
Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur. Selenium ile geliştirmek istediğimiz test otomasyonlarında 
locator’ları kullanarak ilgili alanlara veri gönderebilir, tıklama işlemi yaptırabilir, var olan içeriği temizleyebiliriz. 
Bunlar ‘By’ objesi olarak oluşturulur. En yaygın locator çeşitleri;ID, Name, ClassName, TagName, LinkText, CssSelector, XPath 'dir
"""

# -------------------------------------------------------------------------------------------------------------------------------------

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

# ----- Selenium'da BAZI FONKSİYONLAR -----
    # GET()
# Websitesini açmak için get() kullanılır.Parantezler içerisine girilmek istenilen websitesinin adresi tırnak içerisinde yazılır.
driver.get("https://www.saucedemo.com/")


    # BACK()
# Websitesine girdikten sonra başka bir sayfaya gidildiğinde geri dönmek için back() kullanılır.
driver.back()


    # REFRESH()
# Websitesine girdikten sonra yenilemek için refresh() kullanılır.
driver.refresh()


    # CLOSE() ve QUİT()
# Websitesine giridkten sonra birkaç sayfa daha açtığımızı düşünelim;
    # -Sadece açılan bir sayfayı (sekmeyi) kapatmak için -> close() kullanılır.
    # -Tüm açılan pencereleri (yani tarayıcıyı) kapatmak için -> quit() kullanılır.
driver.close() # Sadece sekmeyi kapatır.
driver.quit() # Tüm tarayıcıyı kapatır.

    # MAXİMİZE_WİNDOW() ve SET_WİNDOW_SİZE 
# Açılan websitesine tam ekran yapmak istersek eğer:
driver.maximize_window()
# Açılan websitesinin boyutlarını kendimiz belirlemek istersek eğer:
driver.set_window_size(800, 600)

    # SAVE_SCREENSHOT() 
# Açılan sayfanın ekran görüntüsünü almak için kullanılır. Alınacak olan ekran görüntüsünün kaydedilecek alanının ismi ve uzantısını 
# parantez içine yazmak zorunludur. Eğer ekran görüntüsü alınabilirse TRUE alınamazsa FALSE döndürür.
driver.save_screenshot("home/ayahmet/test.png")

    # PAGE_SOURCE 
# Açtığımız sayfanın kaynak kodunu ulaşmak istersek kullanırız.
driver.page_source

# ----- Selenium'da Aksiyonlar -----
    # FİND_ELEMENT 
# Açtığımız web sitesindeki bir ögeyi bulmak için kullanılır.  
driver.find_element(By.ID, "password") # Id'si password olan alanı getirir.

    # SEND_KEYS()
# Açtığımız websitesine metin gönderme işlemleri için kullanılır.
firstResult = driver.find_element(By.ID, "user-name")
firstResult.send_keys("Hello World")

sleep(5) # Sistemin 5sn boyunca durmasını ve daha sonra devam etmesini sağlar

    #CLEAR()
#Açtığımız websitesinde belirttiğimiz alanı temizler.
firstResult.clear() # Yukarıda Hello World yazmıştık onu siler.

    # CLİCK() 
# Açtığımız sayfada tıklama işlemi yapmak için kullanılır.
searchButton = driver.find_element(By.ID, "login-button")
searchButton.click()

    # SUBMİT()
# Açtığımız sayfaya bir forum göndermek için kullanılır.
firstResult.send_keys("some text") # some text'i
firstResult.submit() # böyle yaparak açtığımız sayfaya göndeririz

    # SCROLL()
# Açtığımız sayfayı aşağı yukarı kaydırmak için kullanılır.

    # CURRENT_URL
# Gidilen bir web sayfasına yeni bir url ekler.
driver.get("https://www.saucedemo.com/")
driver.current_url == "/inventory.html" #çıktı => "https://www.saucedemo.com/inventory.html" adresine gider sistemimiz.
driver.current_url == "https://www.google.com.tr" #çıktı => "https://www.google.com.tr" adresine gider sistemimiz.