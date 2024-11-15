import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
#driver = webdriver.ChromiumEdge(executable_path="C:\\kkk\\newfolder\\msedgedriver.exe")

driver.get("https://www.primevideo.com/")
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver , 10)

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

driver.find_element(By.XPATH, "(//button[@aria-label='Search Prime Video'])[1]").click()
search_name = input("Enter the name to be searched : ")
driver.find_element(By.ID, "pv-search-nav").send_keys(search_name)

driver.find_element(By.ID, "pv-search-nav").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Vettaiyan']").click()
time.sleep(2)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a[aria-label='Watch Trailer']"))).click()
time.sleep(10)

if menu.is_displayed() is True:
    action.move_to_element(menu).perform()
    item1 = driver.find_element(By.XPATH, "//span[text()='Sign out']")
    action.move_to_element(item1).click().perform()
    print("sign out done successfully")
else:
    print("screen is not moved back to homepage")

time.sleep(2)



