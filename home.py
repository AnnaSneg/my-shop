"""
Home: добавление комментария
1. Откройте http://practice.automationtesting.in/
2. Проскролльте страницу вниз на 600 пикселей
3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
4. Нажмите на вкладку "REVIEWS"
5. Поставьте 5 звёзд
6. Заполните поле "Review" сообщением: "Nice book!"
7. Заполните поле "Name"
8. Заполните "Email"
9. Нажмите на кнопку "SUBMIT"
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 100);")

selenium_ruby = driver.find_element_by_css_selector(".woocommerce-LoopProduct-link h3")
selenium_ruby.click()

reviews = driver.find_element_by_css_selector("[href='#tab-reviews']")
reviews.click()

star_5 = driver.find_element_by_class_name("star-5")
star_5.click()

comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")

name = driver.find_element_by_id("author")
name.send_keys("Anna")

email = driver.find_element_by_id("email")
email.send_keys("anna@gmail.ru")

submit = driver.find_element_by_id("submit")
submit.click()

driver.quit()