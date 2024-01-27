# Домашня робота
# Створити новий проект та додати до нього Selenium.
# Написати автоматизацію яка заходить на 10 сайтів,
# та натискає на мінімум 3 кнопки меню,
# в кожному з них.
# По аналогії з Lesson_9_3


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

sites = ["https://kronas.com.ua/", "https://www.agromat.ua/", "https://www.unsplash.com/", "https://cosmo-multimall.com/", "https://www.azi.com.ua/", "https://www.lemon.kiev.ua/", "https://www.school197.net.ua/", "https://www.dou.ua/", "https://www.dev.ua/", "https://www.itc.ua/"]
for url in sites:
    driver.get(url)
    time.sleep(3)

    if url == "https://kronas.com.ua/":
        menu1_button = driver.find_element("xpath", "/html/body/main/header/nav/div[1]/a")
        menu1_button.click()
        time.sleep(3)

        menu2_button = driver.find_element("xpath", "/html/body/main/header/nav/div[2]/a")
        menu2_button.click()
        time.sleep(3)

        menu3_button_button = driver.find_element("xpath", "/html/body/main/header/nav/div[3]/a")
        menu3_button_button.click()
        time.sleep(3)

    elif url == "https://www.dou.ua/":
        forum_button = driver.find_element("xpath", "/html/body/div[1]/header/ul/li[3]/a")
        forum_button.click()
        time.sleep(3)

        strip_button = driver.find_element("xpath", "/html/body/div[1]/header/ul/li[4]/a")
        strip_button.click()
        time.sleep(3)

        salaries_button = driver.find_element("xpath", "/html/body/div[1]/header/ul/li[5]/a")
        salaries_button.click()
        time.sleep(3)

    elif url == "https://www.dev.ua/":
        pettech_button = driver.find_element("xpath", "/html/body/div[2]/header/div[1]/nav/a[3]")
        pettech_button.click()
        time.sleep(3)

        gamedev_button = driver.find_element("xpath", "/html/body/div[2]/header/div[1]/nav/a[4]")
        gamedev_button.click()
        time.sleep(3)

        money_button = driver.find_element("xpath", "/html/body/div[2]/header/div[1]/nav/a[5]")
        money_button.click()
        time.sleep(3)

    elif url == "https://www.itc.ua/":
        news_button = driver.find_element("xpath", "/html/body/div[3]/header/div[1]/ul/li[3]/a")
        news_button.click()
        time.sleep(3)

        rewiew_button = driver.find_element("xpath", "/html/body/div[3]/header/div[1]/ul/li[4]/a")
        rewiew_button.click()
        time.sleep(3)

        blogs_button = driver.find_element("xpath", "/html/body/div[3]/header/div[1]/ul/li[6]/a")
        blogs_button.click()
        time.sleep(3)

    elif url == "https://www.lemon.kiev.ua/":
        calendar_button = driver.find_element("xpath", "/html/body/div/div[1]/div[3]/div/div[3]/nav/ul/li[3]/a")
        calendar_button.click()
        time.sleep(3)

        rent_button = driver.find_element("xpath", "/html/body/div/div[1]/div[3]/div/div[3]/nav/ul/li[4]/a")
        rent_button.click()
        time.sleep(3)

        master_class_button = driver.find_element("xpath", "/html/body/div/div[1]/div[3]/div/div[3]/nav/ul/li[2]/a")
        master_class_button.click()
        time.sleep(3)

    elif url == "https://www.school197.net.ua/":
        about_button = driver.find_element("xpath", "/html/body/div[1]/header/div[3]/div/nav/div/ul/li[1]/a")
        about_button.click()
        time.sleep(3)

        for_students_button = driver.find_element("xpath", "/html/body/div[1]/header/div[3]/div/nav/div/ul/li[2]/a")
        for_students_button.click()
        time.sleep(3)

        for_parents_button = driver.find_element("xpath", "/html/body/div[1]/header/div[3]/div/nav/div/ul/li[3]/a")
        for_parents_button.click()
        time.sleep(3)

    elif url == "https://www.azi.com.ua/":
        face_button = driver.find_element("xpath", "/html/body/main/header/div[3]/ul/li[2]/a")
        face_button.click()
        time.sleep(3)

        eyes_button = driver.find_element("xpath", "/html/body/main/header/div[3]/ul/li[3]/a")
        eyes_button.click()
        time.sleep(3)

        makeup_button = driver.find_element("xpath", "/html/body/main/header/div[3]/ul/li[4]/a")
        makeup_button.click()
        time.sleep(3)

    elif url == "https://cosmo-multimall.com/":
        menu_button = driver.find_element("xpath", "/html/body/div[1]/div/header/div/div/div[2]/ul/li[2]/a/div/div/span")
        menu_button.click()
        time.sleep(3)

        answer_button = driver.find_element("xpath", "/html/body/div[1]/div/header/div/div/div[2]/ul/li[3]/a/div/div/span")
        answer_button.click()
        time.sleep(3)

        main_button = driver.find_element("xpath", "/html/body/div[1]/div/header/div/div/div[2]/ul/li[4]/a/div/div/span")
        main_button.click()
        time.sleep(3)

    elif url == "https://www.unsplash.com/":
        aditorial_button = driver.find_element("xpath", "/html/body/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/ul/li[5]/a")
        aditorial_button.click()
        time.sleep(3)

        minimal_button = driver.find_element("xpath", "/html/body/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/ul/li[3]/a")
        minimal_button.click()
        time.sleep(3)

        wallpapers_button = driver.find_element("xpath", "/html/body/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/ul/li[4]/a")
        wallpapers_button.click()
        time.sleep(3)

    elif url == "https://www.agromat.ua/":
        menu1_button = driver.find_element("xpath", "/html/body/header/div[2]/div/div/div[2]/div[3]/a[1]")
        menu1_button.click()
        time.sleep(3)

        menu2_button = driver.find_element("xpath", "/html/body/header/div[2]/div/div/div[2]/div[3]/a[2]/span[2]")
        menu2_button.click()
        time.sleep(3)

        menu3_button_button = driver.find_element("xpath", "/html/body/header/div[2]/div/div/div[2]/div[3]/div[1]")
        menu3_button_button.click()
        time.sleep(3)

time.sleep(3)
