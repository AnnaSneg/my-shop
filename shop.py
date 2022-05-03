"""
Shop: отображение страницы товара
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте книгу "HTML 5 Forms"
5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
"""

# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_acc = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("anna@gmail.ru")
#
# password = driver.find_element_by_id("password")
# password.send_keys("_!AnnaLadim123_")
#
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
#
# html5_book = driver.find_element_by_css_selector(".post-181 h3")
# html5_book.click()
#
# header = driver.find_element_by_class_name("product_title")
# header_text = header.text
# assert "HTML5 Forms" in header_text
#
# driver.quit()

"""
Shop: количество товаров в категории
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте категорию "HTML"
5. Добавьте тест, что отображается три товара
"""

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_acc = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("anna@gmail.ru")
#
# password = driver.find_element_by_id("password")
# password.send_keys("_!AnnaLadim123_")
#
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
#
# html_category = driver.find_element_by_css_selector(".cat-item-19 > a")
# html_category.click()
#
# quantity = driver.find_elements_by_css_selector(".masonry-done li")
# assert len(quantity) == 3
#
# driver.quit()

"""
Shop: сортировка товаров
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
• Используйте проверку по value
5. Отсортируйте товары по цене от большей к меньшей
• в селекторах используйте класс Select
6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
• Используйте проверку по value
"""
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_acc = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("anna@gmail.ru")
#
# password = driver.find_element_by_id("password")
# password.send_keys("_!AnnaLadim123_")
#
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
#
# order_menu = driver.find_element_by_class_name("orderby")
# order_menu.click()
# order_1 = driver.find_element_by_css_selector("[value='menu_order']")
# order_1_checked = order_1.get_attribute("selected")
# assert order_1_checked is not None
#
# order = driver.find_element_by_class_name("orderby")
# select = Select(order)
# select.select_by_value("price-desc")
#
# driver.quit()

"""
Shop: отображение, скидка товара
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте книгу "Android Quick Start Guide"
5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
7. Добавьте явное ожидание и нажмите на обложку книги
• Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа
"""

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_acc = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("anna@gmail.ru")
#
# password = driver.find_element_by_id("password")
# password.send_keys("_!AnnaLadim123_")
#
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
#
# book = driver.find_element_by_css_selector(".post-169 h3")
# book.click()
#
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
#
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
#
# open_cover = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169 img")))
# open_cover.click()
#
# close_cover = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_cover.click()
#
# driver.quit()

"""
Shop: проверка цены в корзине
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop"
3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00" 
• Используйте для проверки assert
5. Перейдите в корзину
6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
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
#
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
#
# book_html5 = driver.find_element_by_css_selector(".button.alt")
# book_html5.click()
#
# item = driver.find_element_by_class_name("cartcontents")
# item_text = item.text
# assert item_text == "1 Item"
#
# cost = driver.find_element_by_class_name("amount")
# cost_text = cost.text
# assert cost_text == "₹180.00"
#
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
#
# subtotal = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-price .woocommerce-Price-amount"), "₹180.00"))
# total = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))
#
# driver.quit()

"""
Shop: работа в корзине
Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop"
3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
• Перед добавлением первой книги, проскролльте вниз на 300 пикселей
• После добавления 1-й книги добавьте sleep
4. Перейдите в корзину
5. Удалите первую книгу
• Перед удалением добавьте sleep
6. Нажмите на Undo (отмена удаления)
7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
• Предварительно очистите поле с помощью локатор_поля.clear()
8. Нажмите на кнопку "UPDATE BASKET" 
9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
10. Нажмите на кнопку "APPLY COUPON"
• Перед нажатимем добавьте sleep
11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
"""

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 950);")
#
# book_html5 = driver.find_element_by_css_selector(".post-181 .ajax_add_to_cart")
# book_html5.click()
#
# time.sleep(5)
# book_js = driver.find_element_by_css_selector(".post-180 .ajax_add_to_cart")
# book_js.click()
#
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
#
# time.sleep(5)
# delete = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a")
# delete.click()
#
# time.sleep(5)
# undo = driver.find_element_by_css_selector(".woocommerce-message a")
# undo.click()
#
# quantity = driver.find_element_by_css_selector("tr:nth-child(1) input")
# quantity.clear()
# quantity.send_keys("3")
#
# update = driver.find_element_by_css_selector("[name='update_cart']")
# update.click()
#
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == "3"
#
# time.sleep(5)
#
# coupon = driver.find_element_by_css_selector("[name='apply_coupon']")
# coupon.click()
#
# time.sleep(5)
# enter_coupon = driver.find_element_by_css_selector(".woocommerce li")
# enter_coupon_text = enter_coupon.text
# assert enter_coupon_text == "Please enter a coupon code."
#
# driver.quit()

"""
Shop: покупка товара
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
3. Добавьте в корзину книгу "HTML5 WebApp Development"
4. Перейдите в корзину
5. Нажмите "PROCEED TO CHECKOUT"
• Перед нажатием, добавьте явное ожидание
6. Заполните все обязательные поля
• Перед заполнением first name, добавьте явное ожидание
• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
7. Выберите способ оплаты "Check Payments"
• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
8. Нажмите PLACE ORDER
9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

book_html5 = driver.find_element_by_css_selector(".post-181 .ajax_add_to_cart")
book_html5.click()

cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()

checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout.click()
first_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Anna")

last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Annas")

email = driver.find_element_by_id("billing_email")
email.send_keys("anna@gmail.ru")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("01234567")

country = driver.find_element_by_id("s2id_billing_country")
country.click()
country_sel = driver.find_element_by_id("s2id_autogen1_search")
country_sel.send_keys("Denmark")
driver.find_element_by_id("select2-results-1").click()

address = driver.find_element_by_id("billing_address_1")
address.send_keys("First street 5, apt. 2")

postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("12345")

city = driver.find_element_by_id("billing_city")
city.send_keys("Copenhagen")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)

payments = driver.find_element_by_id("payment_method_cheque")
payments.click()

order = driver.find_element_by_id("place_order")
order.click()

thank_you = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_payments = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method > strong"), "Check Payments"))

driver.quit()

