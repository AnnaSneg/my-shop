"""
Registration_login: регистрация аккаунта
1. Откройте http://practice.automationtesting.in/
2. Нажмите на вкладку "My Account Menu"
3. В разделе "Register", введите email для регистрации
4. В разделе "Register", введите пароль для регистрации
• составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
• почту и пароль сохраните, потребуюутся в дальнейшем
5. Нажмите на кнопку "Register"
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_acc = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
#
# email = driver.find_element_by_id("reg_email")
# email.send_keys("anna@gmail.ru")
#
# password = driver.find_element_by_id("reg_password")
# password.send_keys("_!AnnaLadim123_")
#
# register = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='register']")))
# register.click()
#
# driver.quit()

"""
Registration_login: логин в систему
1. Откройте http://practice.automationtesting.in/
2. Нажмите на вкладку "My Account Menu"
3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
5. Нажмите на кнопку "Login"
6. Добавьте проверку, что на странице есть элемент "Logout"
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

my_acc = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
my_acc.click()

email = driver.find_element_by_id("username")
email.send_keys("anna@gmail.ru")

password = driver.find_element_by_id("password")
password.send_keys("_!AnnaLadim123_")

login = driver.find_element_by_css_selector("[name='login']")
login.click()

logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout > a")
logout_text = logout.text
assert "Logout" in logout_text

driver.quit()