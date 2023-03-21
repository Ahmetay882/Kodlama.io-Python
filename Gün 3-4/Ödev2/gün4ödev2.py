from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Test_Sauce:

    def test_task1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        errorMessage = "Epic sadface: Username is required"
        print(errorMessage)
        sleep(100)


    def test_task2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        sleep(2)

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        errorMessage = "Epic sadface: Password is required" 
        print(errorMessage)
        sleep(100)


    def test_task3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        sleep(2)

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        errorMessage = "Epic sadface: Sorry, this user has been locked out."
        print(errorMessage)
        sleep(100) 


    def test_task4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        sleep(2)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()

        errorIcon = driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()
        sleep(100)


    def test_task5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()
        driver.current_url == "/inventory.html"
        sleep(100)


    def test_task6(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()

        itemList = driver.find_elements(By.CLASS_NAME, "inventory_item")
        result = len(itemList) == 6
        print(f"Ürün sayisi {result}")


test = Test_Sauce()

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# test.test_task1() 

# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# test.test_task2()

# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# test.test_task3()

# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan 
# uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
test.test_task4()

# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# test.test_task5()

# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
# test.test_task6()