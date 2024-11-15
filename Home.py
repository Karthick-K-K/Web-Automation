import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

#driver = webdriver.ChromiumEdge(executable_path="C:\\kkk\\newfolder\\msedgedriver.exe")
driver.maximize_window()


driver.get("https://www.primevideo.com/")
time.sleep(2)
wait = WebDriverWait(driver , 10)

#driver.find_element(By.XPATH, "//button[@aria-label='Profile, Settings, and Account']").click()

action = ActionChains(driver)
menu = driver.find_element(By.XPATH, "//button[@aria-label='Profile, Settings, and Account']")
action.move_to_element(menu).perform()
# select_items = driver.find_elements(By.XPATH, "//div[@class='secondary-nav__row multi-columns']/div[3]/a")
# print(len(select_items))
# for i in select_items:
#     txt = i.find_element(By.XPATH, "span").text
#     print(txt)
#     if txt == "Sign out":
#         item = i
#         break
item = driver.find_element(By.XPATH, "//span[text()='Sign In']")
action.move_to_element(item).click().perform()
time.sleep(2)
driver.find_element(By.NAME, "email").send_keys("karthick.krishnasetty@ovyo.com") 
driver.find_element(By.ID, "continue").click()
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("kk@may23")

driver.find_element(By.ID, "signInSubmit").click()
time.sleep(3)

# action = ActionChains(driver)
menu = driver.find_element(By.XPATH, "//button[@aria-label='Profile, Settings, and Account']")
action.move_to_element(menu).perform()
print("sign in done successfully")
#wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Sign Out']")))
item1 = driver.find_element(By.XPATH, "//span[text()='Sign out']")
action.move_to_element(item1).click().perform()
print("sign out done successfully")

time.sleep(2)