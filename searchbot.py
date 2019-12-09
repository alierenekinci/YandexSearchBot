from selenium import webdriver
driver_path = "/Users/alierenekinci/Desktop/Python/Machine Learning/Z/chromedriver"  
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

site = 'https://yandex.com.tr/'
text = input('Çabuk ara:')


driver = webdriver.Chrome(executable_path=driver_path)
driver.get(site)
#driver.maximize_window()

# type text
text_area = driver.find_element_by_id('text')
text_area.send_keys(text)


# click submit button
submit_button = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/form/div[2]/button')[0]
submit_button.click()
