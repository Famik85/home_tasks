from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

url = "https://test.mensa.no/"

driver.get(url)

age_1850 = driver.find_element(By.CLASS_NAME, 'ageselect_1850')
age_1850.click()
time.sleep(3)

start_button = driver.find_element(By.ID, 'startTest')
start_button.click()
time.sleep(3)

q1_a1_button = driver.find_element(By.XPATH, '//div[@id="question_0"]//div[@data-answerid="0"]')
q1_a1_button.click()
time.sleep(3)

q2_a5_button = driver.find_element(By.XPATH, '//div[@id="question_1"]//div[@data-answerid="4"]')
q2_a5_button.click()
time.sleep(3)

q3_a6_button = driver.find_element(By.XPATH, '//div[@id="question_2"]//div[@data-answerid="5"]')
q3_a6_button.click()
time.sleep(3)

q4_a6_button = driver.find_element(By.XPATH, '//div[@id="question_3"]//div[@data-answerid="5"]')
q4_a6_button.click()
time.sleep(3)

q5_a4_button = driver.find_element(By.XPATH, '//div[@id="question_4"]//div[@data-answerid="3"]')
q5_a4_button.click()
time.sleep(3)

q6_a5_button = driver.find_element(By.XPATH, '//div[@id="question_5"]//div[@data-answerid="4"]')
q6_a5_button.click()
time.sleep(3)

q7_a5_button = driver.find_element(By.XPATH, '//div[@id="question_6"]//div[@data-answerid="4"]')
q7_a5_button.click()
time.sleep(3)

q8_a3_button = driver.find_element(By.XPATH, '//div[@id="question_7"]//div[@data-answerid="2"]')
q8_a3_button.click()
time.sleep(3)

q9_a4_button = driver.find_element(By.XPATH, '//div[@id="question_8"]//div[@data-answerid="3"]')
q9_a4_button.click()
time.sleep(3)

q10_a4_button = driver.find_element(By.XPATH, '//div[@id="question_9"]//div[@data-answerid="3"]')
q10_a4_button.click()
time.sleep(3)

q11_a1_button = driver.find_element(By.XPATH, '//div[@id="question_10"]//div[@data-answerid="0"]')
q11_a1_button.click()
time.sleep(3)

q12_a3_button = driver.find_element(By.XPATH, '//div[@id="question_11"]//div[@data-answerid="2"]')
q12_a3_button.click()
time.sleep(3)

q13_a2_button = driver.find_element(By.XPATH, '//div[@id="question_12"]//div[@data-answerid="1"]')
q13_a2_button.click()
time.sleep(3)

q14_a1_button = driver.find_element(By.XPATH, '//div[@id="question_13"]//div[@data-answerid="0"]')
q14_a1_button.click()
time.sleep(3)

q15_a6_button = driver.find_element(By.XPATH, '//div[@id="question_14"]//div[@data-answerid="5"]')
q15_a6_button.click()
time.sleep(3)

q16_a2_button = driver.find_element(By.XPATH, '//div[@id="question_15"]//div[@data-answerid="1"]')
q16_a2_button.click()
time.sleep(3)

q17_a4_button = driver.find_element(By.XPATH, '//div[@id="question_16"]//div[@data-answerid="3"]')
q17_a4_button.click()
time.sleep(3)

q18_a3_button = driver.find_element(By.XPATH, '//div[@id="question_17"]//div[@data-answerid="2"]')
q18_a3_button.click()
time.sleep(3)

q19_a1_button = driver.find_element(By.XPATH, '//div[@id="question_18"]//div[@data-answerid="0"]')
q19_a1_button.click()
time.sleep(3)

q20_a2_button = driver.find_element(By.XPATH, '//div[@id="question_19"]//div[@data-answerid="1"]')
q20_a2_button.click()
time.sleep(3)

q21_a1_button = driver.find_element(By.XPATH, '//div[@id="question_20"]//div[@data-answerid="0"]')
q21_a1_button.click()
time.sleep(3)

q22_a3_button = driver.find_element(By.XPATH, '//div[@id="question_21"]//div[@data-answerid="2"]')
q22_a3_button.click()
time.sleep(3)

q23_a2_button = driver.find_element(By.XPATH, '//div[@id="question_22"]//div[@data-answerid="1"]')
q23_a2_button.click()
time.sleep(3)

q24_a4_button = driver.find_element(By.XPATH, '//div[@id="question_23"]//div[@data-answerid="3"]')
q24_a4_button.click()
time.sleep(3)

q25_a3_button = driver.find_element(By.XPATH, '//div[@id="question_24"]//div[@data-answerid="2"]')
q25_a3_button.click()
time.sleep(3)

q26_a2_button = driver.find_element(By.XPATH, '//div[@id="question_25"]//div[@data-answerid="1"]')
q26_a2_button.click()
time.sleep(3)

q27_a4_button = driver.find_element(By.XPATH, '//div[@id="question_26"]//div[@data-answerid="3"]')
q27_a4_button.click()
time.sleep(3)

q28_a1_button = driver.find_element(By.XPATH, '//div[@id="question_27"]//div[@data-answerid="0"]')
q28_a1_button.click()
time.sleep(3)

q29_a3_button = driver.find_element(By.XPATH, '//div[@id="question_28"]//div[@data-answerid="2"]')
q29_a3_button.click()
time.sleep(3)

q30_a2_button = driver.find_element(By.XPATH, '//div[@id="question_29"]//div[@data-answerid="1"]')
q30_a2_button.click()
time.sleep(3)

q31_a1_button = driver.find_element(By.XPATH, '//div[@id="question_30"]//div[@data-answerid="0"]')
q31_a1_button.click()
time.sleep(3)

q32_a1_button = driver.find_element(By.XPATH, '//div[@id="question_31"]//div[@data-answerid="0"]')
q32_a1_button.click()
time.sleep(3)

q33_a3_button = driver.find_element(By.XPATH, '//div[@id="question_32"]//div[@data-answerid="2"]')
q33_a3_button.click()
time.sleep(3)

q34_a1_button = driver.find_element(By.XPATH, '//div[@id="question_33"]//div[@data-answerid="0"]')
q34_a1_button.click()
time.sleep(3)

q35_a4_button = driver.find_element(By.XPATH, '//div[@id="question_34"]//div[@data-answerid="3"]')
q35_a4_button.click()
time.sleep(3)

time.sleep(30)