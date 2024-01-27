from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
driver.get(url)

q1_element = driver.find_element(By.NAME, "q1")
q1_element.send_keys("m")

q2_element = driver.find_element(By.NAME, "q2")
q2_element.send_keys("15")

q3_element = driver.find_element(By.NAME, "q3")
q3_element.send_keys("8")

q4_element = driver.find_element(By.NAME, "q4")
q4_element.send_keys("6")

q5_element = driver.find_element(By.NAME, "q5")
q5_element.send_keys("5")

q6_element = driver.find_element(By.NAME, "q6")
q6_element.send_keys("4")

q7_element = driver.find_element(By.NAME, "q7")
q7_element.send_keys("1")

q8_element = driver.find_element(By.NAME, "q8")
q8_element.send_keys("2")

q9_c_element = driver.find_element(By.XPATH, '//input[@name="q9" and @value="c"] ')
q9_c_element.click()

q10_b_element = driver.find_element(By.XPATH, '//input[@name="q10" and @value="b"] ')
q10_b_element.click()

q11_c_element = driver.find_element(By.XPATH, '//input[@name="q11" and @value="c"] ')
q11_c_element.click()

q12_d_element = driver.find_element(By.XPATH, '//input[@name="q12" and @value="d"] ')
q12_d_element.click()

q13_d_element = driver.find_element(By.XPATH, '//input[@name="q13" and @value="d"] ')
q13_d_element.click()

q14_c_element = driver.find_element(By.XPATH, '//input[@name="q14" and @value="c"] ')
q14_c_element.click()

q15_c_element = driver.find_element(By.XPATH, '//input[@name="q15" and @value="c"] ')
q15_c_element.click()

q16_d_element = driver.find_element(By.XPATH, '//input[@name="q16" and @value="d"] ')
q16_d_element.click()

q17_b_element = driver.find_element(By.XPATH, '//input[@name="q17" and @value="b"] ')
q17_b_element.click()

q18_a_element = driver.find_element(By.XPATH, '//input[@name="q18" and @value="a"] ')
q18_a_element.click()

q19_a_element = driver.find_element(By.XPATH, '//input[@name="q19" and @value="a"] ')
q19_a_element.click()
q19_d_element = driver.find_element(By.XPATH, '//input[@name="q19" and @value="d"] ')
q19_d_element.click()

q20_b_element = driver.find_element(By.XPATH, '//input[@name="q20" and @value="b"] ')
q20_b_element.click()
q20_c_element = driver.find_element(By.XPATH, '//input[@name="q20" and @value="c"] ')
q20_c_element.click()

q21_a_element = driver.find_element(By.XPATH, '//input[@name="q21" and @value="a"] ')
q21_a_element.click()
q21_d_element = driver.find_element(By.XPATH, '//input[@name="q21" and @value="d"] ')
q21_d_element.click()

q22_b_element = driver.find_element(By.XPATH, '//input[@name="q22" and @value="b"] ')
q22_b_element.click()
q22_d_element = driver.find_element(By.XPATH, '//input[@name="q22" and @value="d"] ')
q22_d_element.click()

q23_d_element = driver.find_element(By.XPATH, '//input[@name="q23" and @value="d"] ')
q23_d_element.click()

q24_c_element = driver.find_element(By.XPATH, '//input[@name="q24" and @value="c"] ')
q24_c_element.click()

q25_b_element = driver.find_element(By.XPATH, '//input[@name="q25" and @value="b"] ')
q25_b_element.click()

q26_c_element = driver.find_element(By.XPATH, '//input[@name="q26" and @value="c"] ')
q26_c_element.click()

q27_b_element = driver.find_element(By.XPATH, '//input[@name="q27" and @value="b"] ')
q27_b_element.click()

q28_d_element = driver.find_element(By.XPATH, '//input[@name="q28" and @value="d"] ')
q28_d_element.click()

q29_c_element = driver.find_element(By.XPATH, '//input[@name="q29" and @value="c"] ')
q29_c_element.click()

q30_a_element = driver.find_element(By.XPATH, '//input[@name="q30" and @value="a"] ')
q30_a_element.click()

q31_c_element = driver.find_element(By.XPATH, '//input[@name="q31" and @value="c"] ')
q31_c_element.click()

q32_d_element = driver.find_element(By.XPATH, '//input[@name="q32" and @value="d"] ')
q32_d_element.click()

q33_c_element = driver.find_element(By.XPATH, '//input[@name="q33" and @value="c"] ')
q33_c_element.click()

time.sleep(5)
finish_button = driver.find_element(By.XPATH, '//input[@value="FINISHED"]')
finish_button.click()

time.sleep(300)