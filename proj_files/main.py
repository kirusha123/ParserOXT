# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()
# driver.get("http://www.oxt.me")

# # driver.close()

# # wait = WebDriverWait(driver, 10)
# # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.form-control.search-inp#search-imp")))


# wait = WebDriverWait(driver, 10)
# h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.form-control.search-inp#search-imp")))
# # print h3.text

# # a = driver.find_element_by_css_selector('input.form-control.search-inp#search-imp')
# h3.click()

# print("All is good")

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url ="https://oxt.me/directory" 

def main():
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(15)
    # for i in range(200):
    #     driver.get(url)
    #     time.sleep(5)
    #     WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"table tr td:nth-child(1) a")))   
    #     lst = driver.find_elements_by_css_selector("table tr td:nth-child(1) a")
    #     lst[i].click()
    #     time.sleep(5)
    lst = driver.find_elements_by_css_selector("table tr td:nth-child(1) a")
    el_count = len(lst)
    print(el_count)


    for i in range(el_count):
        driver.get(url)
        time.sleep(8)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"table tr td:nth-child(1) a")))
        lst = driver.find_elements_by_css_selector("table tr td:nth-child(1) a")
        lst[i].click()
        time.sleep(15)
    driver.quit()
    # btn = driver.find_element_by_css_selector("")

if __name__ == "__main__":
    main()