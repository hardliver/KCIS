# https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 找到符合電腦 Chrome 的版本
# https://chromedriver.chromium.org/downloads
driver_path = './chromedriver'  # 
brower = webdriver.Chrome(driver_path)

url = 'https://www.ygfamily.com/'
brower.get(url)

# print('標題', brower.title)
# print('網址', brower.current_url)
# print('內容', brower.page_source[:50])
# print('視窗', brower.get_window_rect())

# brower.save_screenshot('./screenshop.png')
# time.sleep(3)
# brower.set_window_rect(200, 100, 500, 250)  # 改變視窗位址與大小
# time.sleep(3)
# brower.fullscreen_window()

xpath = '//*[@id="nav"]/ul/li[3]/a'
b = brower.find_element(By.XPATH, xpath)
print('##########')
print(b)
print(b.text)
print(b.__dir__())


# time.sleep(3)
# brower.close()  # 關閉分頁
brower.quit()   # 關閉瀏覽器
